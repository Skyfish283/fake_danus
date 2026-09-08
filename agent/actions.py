"""Structured actions returned by the planner, and their graph execution.

The planner never touches Python objects. It returns a list of actions, which
are validated here and then executed deterministically: graph mutations in
this module, dispatching actions (tasks, searches, finishing) by the
supervisor.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

from ..graph.graph import NODE_TYPES, RELATIONS, STATUSES
from ..workers.base import PROMPT_ROLES, WORKER_SLOTS

ACTION_TYPES = (
    "ADD_NODE",
    "UPDATE_NODE",
    "ADD_EDGE",
    "ASSIGN_TASK",
    "CANCEL_TASK",
    "SEARCH_PAPERS",
    "GET_PAPER",
    "FINISH",
)

GRAPH_ACTIONS = ("ADD_NODE", "UPDATE_NODE", "ADD_EDGE")

SEARCH_SOURCES = ("openalex", "semantic_scholar", "arxiv")

# Uppercase type names are what the Gemini structured-output schema expects.
ACTION_SCHEMA: dict[str, Any] = {
    "type": "OBJECT",
    "required": ["reasoning", "actions"],
    "properties": {
        "reasoning": {
            "type": "STRING",
            "description": "One or two sentences on why these actions were chosen.",
        },
        "actions": {
            "type": "ARRAY",
            "description": "Actions to execute, in order. May be empty.",
            "items": {
                "type": "OBJECT",
                "required": ["type"],
                "properties": {
                    "type": {"type": "STRING", "enum": list(ACTION_TYPES)},
                    "node_type": {
                        "type": "STRING",
                        "enum": list(NODE_TYPES),
                        "description": "ADD_NODE: what kind of node this is.",
                    },
                    "content": {
                        "type": "STRING",
                        "description": "ADD_NODE/UPDATE_NODE: self-contained mathematical content.",
                    },
                    "status": {
                        "type": "STRING",
                        "enum": list(STATUSES),
                        "description": "ADD_NODE/UPDATE_NODE: research status of the claim.",
                    },
                    "node_id": {
                        "type": "STRING",
                        "description": "UPDATE_NODE: which node to update.",
                    },
                    "note": {
                        "type": "STRING",
                        "description": "UPDATE_NODE: a short note appended to the node's history.",
                    },
                    "source": {
                        "type": "STRING",
                        "description": "ADD_EDGE: id of the node the edge starts at.",
                    },
                    "target": {
                        "type": "STRING",
                        "description": "ADD_EDGE: id of the node the edge points to.",
                    },
                    "relation": {"type": "STRING", "enum": list(RELATIONS)},
                    "worker": {
                        "type": "STRING",
                        "enum": list(WORKER_SLOTS),
                        "description": (
                            "ASSIGN_TASK: which worker slot. All slots are "
                            "flexible: flex_1 through flex_6."
                        ),
                    },
                    "role": {
                        "type": "STRING",
                        "enum": list(PROMPT_ROLES),
                        "description": (
                            "ASSIGN_TASK: REQUIRED on every slot (searcher, "
                            "toy_example, counterexample, decomposer, sketcher, "
                            "or verifier)."
                        ),
                    },
                    "task": {
                        "type": "STRING",
                        "description": "ASSIGN_TASK: a specific instruction referencing node ids.",
                    },
                    "focus_nodes": {
                        "type": "ARRAY",
                        "items": {"type": "STRING"},
                        "description": "ASSIGN_TASK: node ids the worker should be shown.",
                    },
                    "task_id": {
                        "type": "STRING",
                        "description": "CANCEL_TASK: id of the running task to cancel.",
                    },
                    "query": {
                        "type": "STRING",
                        "description": "SEARCH_PAPERS: the literature search query.",
                    },
                    "search_source": {
                        "type": "STRING",
                        "enum": list(SEARCH_SOURCES),
                        "description": "SEARCH_PAPERS: which API to use. Defaults to openalex.",
                    },
                    "paper_id": {
                        "type": "STRING",
                        "description": "GET_PAPER: the paper id from a previous search result.",
                    },
                    "summary": {
                        "type": "STRING",
                        "description": "FINISH: the final report for the human researcher.",
                    },
                },
            },
        },
    },
}


@dataclass
class Action:
    """One planner action, with tolerant access to its fields."""

    type: str
    raw: dict[str, Any] = field(default_factory=dict)

    def get(self, *names: str, default: Any = "") -> Any:
        for name in names:
            value = self.raw.get(name)
            if value not in (None, ""):
                return value
        return default

    def describe(self) -> str:
        if self.type == "ADD_NODE":
            return f"ADD_NODE ({self.get('status', default='IDEA')}) {_clip(self.get('content'))}"
        if self.type == "UPDATE_NODE":
            return f"UPDATE_NODE {self.get('node_id')} -> {self.get('status', default='(content)')}"
        if self.type == "ADD_EDGE":
            return (
                f"ADD_EDGE {self.get('source', 'from')} "
                f"-{self.get('relation', default='related_to')}-> {self.get('target', 'to')}"
            )
        if self.type == "ASSIGN_TASK":
            slot = self.get("worker")
            role = self.get("role")
            if role and str(role) != str(slot):
                return f"ASSIGN_TASK {slot} as {role}: {_clip(self.get('task'))}"
            return f"ASSIGN_TASK {slot}: {_clip(self.get('task'))}"
        if self.type == "CANCEL_TASK":
            return f"CANCEL_TASK {self.get('task_id')}"
        if self.type == "SEARCH_PAPERS":
            return (
                f"SEARCH_PAPERS [{self.get('search_source', 'source', default='openalex')}] "
                f"{_clip(self.get('query'))}"
            )
        if self.type == "GET_PAPER":
            return f"GET_PAPER {self.get('paper_id')}"
        if self.type == "FINISH":
            return "FINISH"
        return self.type


def _clip(text: Any, limit: int = 90) -> str:
    text = str(text).replace("\n", " ").strip()
    return text if len(text) <= limit else text[: limit - 3] + "..."


class ActionParseError(ValueError):
    """The planner's output could not be read as an action list."""


def _extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text).strip()
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ActionParseError(f"no JSON object found: {exc}") from exc
        try:
            payload = json.loads(match.group(0))
        except json.JSONDecodeError as exc2:
            raise ActionParseError(f"invalid JSON: {exc2}") from exc2
    if not isinstance(payload, dict):
        raise ActionParseError("top-level JSON value is not an object")
    return payload


def parse_actions(text: str) -> tuple[str, list[Action]]:
    """Parse the planner's JSON reply into a reasoning string and actions.

    Unknown action types and unknown fields are dropped rather than raising, so
    one malformed action cannot end the run.
    """
    payload = _extract_json(text)
    reasoning = str(payload.get("reasoning", "") or "").strip()
    raw_actions = payload.get("actions", [])
    if not isinstance(raw_actions, list):
        raise ActionParseError("'actions' is not a list")

    actions: list[Action] = []
    for item in raw_actions:
        if not isinstance(item, dict):
            continue
        action_type = str(item.get("type", "")).strip().upper()
        if action_type not in ACTION_TYPES:
            continue
        actions.append(Action(type=action_type, raw=item))
    return reasoning, actions


def apply_graph_action(graph, action: Action, *, author: str = "planner") -> str:
    """Execute a graph-mutating action. Returns a human-readable result line."""
    if action.type == "ADD_NODE":
        content = str(action.get("content")).strip()
        if not content:
            return "ADD_NODE skipped: empty content"
        duplicate = graph.find_identical(content)
        if duplicate:
            return f"ADD_NODE skipped: identical to {duplicate}"
        node_id = graph.add_node(
            node_type=str(action.get("node_type", default="idea")),
            content=content,
            status=str(action.get("status", default="IDEA")),
            created_by=str(action.get("created_by", default=author)),
        )
        return f"added {node_id} ({graph.nodes[node_id]['status']})"

    if action.type == "UPDATE_NODE":
        node_id = str(action.get("node_id", "id")).strip()
        if not graph.exists(node_id):
            return f"UPDATE_NODE skipped: no such node {node_id!r}"
        graph.update_node(
            node_id,
            status=str(action.get("status", default="")) or None,
            content=str(action.get("content", default="")) or None,
            note=str(action.get("note", default="")) or None,
            updated_by=author,
        )
        return f"updated {node_id} -> {graph.nodes[node_id]['status']}"

    if action.type == "ADD_EDGE":
        source = str(action.get("source", "from")).strip()
        target = str(action.get("target", "to")).strip()
        relation = str(action.get("relation", default="related_to"))
        if graph.add_edge(source, target, relation):
            return f"edge {source} -{relation}-> {target}"
        return f"ADD_EDGE skipped: {source} -> {target} (unknown node or duplicate)"

    return f"{action.type} is not a graph action"
