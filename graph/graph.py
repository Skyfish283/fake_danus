"""The research graph: persistent memory of what has been considered.

Deliberately crude - nodes in a dict, edges in a list, persisted as JSON. This
is a research notebook, not a database of verified mathematical facts.
"""

from __future__ import annotations

import re
import time
from typing import Any, Iterable

from .. import config

NODE_TYPES = (
    "problem",
    "approach",
    "idea",
    "lemma",
    "theorem",
    "obstacle",
    "counterexample",
    "question",
    "hypothesis",
    "paper",
    "note",
)

STATUSES = (
    "IDEA",
    "PROMISING",
    "UNVERIFIED",
    "OBSTACLE",
    "DEAD_END",
    "REJECTED",
    "POTENTIALLY_RELEVANT",
)

RELATIONS = (
    "depends_on",
    "related_to",
    "supports",
    "contradicts",
    "motivates",
    "derived_from",
    "similar_to",
    "possible_approach",
    "contains",
    "addresses",
    "blocks",
)

# Statuses whose nodes stay interesting: live work and recorded blockers.
LIVE_STATUSES = ("PROMISING", "IDEA", "UNVERIFIED", "OBSTACLE")

_STATUS_WEIGHT = {
    "PROMISING": 3.0,
    "OBSTACLE": 2.0,
    "UNVERIFIED": 1.5,
    "IDEA": 1.0,
    "POTENTIALLY_RELEVANT": 1.0,
    "DEAD_END": -1.0,
    "REJECTED": -2.0,
}

_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "could", "does",
    "for", "from", "has", "have", "how", "in", "is", "it", "its", "may", "not",
    "of", "on", "or", "should", "that", "the", "then", "there", "this", "to",
    "we", "what", "when", "which", "with", "would", "using", "use", "any",
    "every", "some", "must", "if", "but", "into", "via", "one", "all",
}

_WORD_RE = re.compile(r"[a-z0-9]+")


def _tokens(text: str) -> set[str]:
    return {
        word
        for word in _WORD_RE.findall(text.lower())
        if len(word) > 2 and word not in _STOPWORDS
    }


def _normalise(text: str) -> str:
    return " ".join(_WORD_RE.findall(text.lower()))


class ResearchGraph:
    """Nodes, edges, and the crude retrieval used to build model context."""

    def __init__(self, problem: str = "") -> None:
        self.data: dict[str, Any] = {"problem": problem, "nodes": {}, "edges": []}
        self._counters: dict[str, int] = {}
        self._on_change = None
        if problem:
            self.add_node(
                node_type="problem",
                content=problem,
                status="UNVERIFIED",
                created_by="user",
                node_id="problem",
            )

    # -- persistence hooks --------------------------------------------------

    def set_change_hook(self, hook) -> None:
        """Register a callback fired after every mutation (used to save JSON)."""
        self._on_change = hook

    def _changed(self) -> None:
        if self._on_change is not None:
            self._on_change(self)

    # -- basic accessors ----------------------------------------------------

    @property
    def problem(self) -> str:
        return self.data.get("problem", "")

    @property
    def nodes(self) -> dict[str, dict[str, Any]]:
        return self.data["nodes"]

    @property
    def edges(self) -> list[dict[str, str]]:
        return self.data["edges"]

    def get(self, node_id: str) -> dict[str, Any] | None:
        return self.nodes.get(node_id)

    def exists(self, node_id: str) -> bool:
        return node_id in self.nodes

    def _next_id(self, node_type: str) -> str:
        prefix = node_type if node_type in NODE_TYPES else "note"
        while True:
            self._counters[prefix] = self._counters.get(prefix, 0) + 1
            candidate = f"{prefix}_{self._counters[prefix]}"
            if candidate not in self.nodes:
                return candidate

    # -- mutation -----------------------------------------------------------

    def add_node(
        self,
        *,
        node_type: str,
        content: str,
        status: str = "IDEA",
        created_by: str = "planner",
        node_id: str | None = None,
        extra: dict[str, Any] | None = None,
    ) -> str:
        node_type = node_type if node_type in NODE_TYPES else "note"
        status = status if status in STATUSES else "IDEA"
        node_id = node_id or self._next_id(node_type)

        node: dict[str, Any] = {
            "id": node_id,
            "type": node_type,
            "content": content.strip(),
            "status": status,
            "created_by": created_by,
            "created_at": time.time(),
            "updated_at": time.time(),
            "history": [],
        }
        if extra:
            node.update(extra)
        self.nodes[node_id] = node
        self._changed()
        return node_id

    def update_node(
        self,
        node_id: str,
        *,
        status: str | None = None,
        content: str | None = None,
        note: str | None = None,
        updated_by: str = "planner",
    ) -> bool:
        node = self.nodes.get(node_id)
        if node is None:
            return False

        if status and status in STATUSES and status != node["status"]:
            node["history"].append(
                {"at": time.time(), "by": updated_by, "status_from": node["status"], "status_to": status}
            )
            node["status"] = status
        if content:
            node["content"] = content.strip()
        if note:
            node.setdefault("notes", []).append({"at": time.time(), "by": updated_by, "note": note})
        node["updated_at"] = time.time()
        self._changed()
        return True

    def add_edge(self, source: str, target: str, relation: str) -> bool:
        if source not in self.nodes or target not in self.nodes or source == target:
            return False
        relation = relation if relation in RELATIONS else "related_to"
        edge = {"source": source, "target": target, "relation": relation}
        if edge in self.edges:
            return False
        self.edges.append(edge)
        self._changed()
        return True

    def find_identical(self, content: str) -> str | None:
        """Return the id of a node with textually identical content, if any."""
        target = _normalise(content)
        if not target:
            return None
        for node_id, node in self.nodes.items():
            if _normalise(node["content"]) == target:
                return node_id
        return None

    # -- queries ------------------------------------------------------------

    def by_status(self, *statuses: str) -> list[dict[str, Any]]:
        wanted = set(statuses)
        return [node for node in self.nodes.values() if node["status"] in wanted]

    def neighbours(self, node_id: str) -> list[str]:
        out: list[str] = []
        for edge in self.edges:
            if edge["source"] == node_id:
                out.append(edge["target"])
            elif edge["target"] == node_id:
                out.append(edge["source"])
        return out

    def retrieve(
        self,
        query: str = "",
        *,
        limit: int = 20,
        focus: Iterable[str] = (),
    ) -> list[dict[str, Any]]:
        """Pick a slice of the graph: the problem, focus nodes, obstacles, then
        whatever scores best on keyword overlap, status and recency."""
        selected: dict[str, dict[str, Any]] = {}

        problem_node = self.nodes.get("problem")
        if problem_node is not None:
            selected["problem"] = problem_node

        for node_id in focus:
            node = self.nodes.get(node_id)
            if node is not None:
                selected[node_id] = node
                for neighbour in self.neighbours(node_id):
                    neighbour_node = self.nodes.get(neighbour)
                    if neighbour_node is not None:
                        selected.setdefault(neighbour, neighbour_node)

        for node in self.by_status("OBSTACLE"):
            selected.setdefault(node["id"], node)

        query_tokens = _tokens(query)
        newest = max((n["updated_at"] for n in self.nodes.values()), default=0.0)
        oldest = min((n["updated_at"] for n in self.nodes.values()), default=0.0)
        span = max(newest - oldest, 1.0)

        def score(node: dict[str, Any]) -> float:
            overlap = 0.0
            if query_tokens:
                node_tokens = _tokens(node["content"])
                if node_tokens:
                    overlap = 3.0 * len(query_tokens & node_tokens) / len(query_tokens)
            recency = (node["updated_at"] - oldest) / span
            return overlap + 2.0 * recency + _STATUS_WEIGHT.get(node["status"], 0.0)

        remaining = [n for n in self.nodes.values() if n["id"] not in selected]
        remaining.sort(key=score, reverse=True)
        for node in remaining:
            if len(selected) >= limit:
                break
            selected[node["id"]] = node

        ordered = sorted(selected.values(), key=lambda n: n["created_at"])
        return ordered[:limit] if len(ordered) > limit else ordered

    # -- rendering ----------------------------------------------------------

    def render_nodes(self, nodes: Iterable[dict[str, Any]]) -> str:
        chunks: list[str] = []
        for node in nodes:
            content = node["content"]
            if len(content) > config.MAX_NODE_CHARS_IN_CONTEXT:
                content = content[: config.MAX_NODE_CHARS_IN_CONTEXT] + " [...truncated]"
            header = f"[{node['id']}] ({node['type']}, {node['status']}, by {node['created_by']})"
            edges = self._render_edges_for(node["id"])
            chunks.append(f"{header}\n{content}" + (f"\n  links: {edges}" if edges else ""))
        return "\n\n".join(chunks)

    def _render_edges_for(self, node_id: str) -> str:
        parts = [
            f"{edge['relation']} -> {edge['target']}"
            for edge in self.edges
            if edge["source"] == node_id
        ]
        parts += [
            f"{edge['source']} -{edge['relation']}-> this"
            for edge in self.edges
            if edge["target"] == node_id
        ]
        return "; ".join(parts[:8])

    def context_for(self, query: str = "", *, limit: int = 20, focus: Iterable[str] = ()) -> str:
        nodes = self.retrieve(query, limit=limit, focus=focus)
        if not nodes:
            return ""
        return self.render_nodes(nodes)

    def status_counts(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for node in self.nodes.values():
            counts[node["status"]] = counts.get(node["status"], 0) + 1
        return counts

    def stats_line(self) -> str:
        counts = self.status_counts()
        parts = [f"{status}={counts[status]}" for status in STATUSES if status in counts]
        return f"{len(self.nodes)} nodes, {len(self.edges)} edges" + (
            f" ({', '.join(parts)})" if parts else ""
        )

    # -- serialisation ------------------------------------------------------

    def to_dict(self) -> dict[str, Any]:
        return self.data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ResearchGraph":
        graph = cls()
        graph.data = {
            "problem": data.get("problem", ""),
            "nodes": data.get("nodes", {}),
            "edges": data.get("edges", []),
        }
        for node_id in graph.nodes:
            prefix, _, number = node_id.rpartition("_")
            if prefix and number.isdigit():
                graph._counters[prefix] = max(graph._counters.get(prefix, 0), int(number))
        return graph
