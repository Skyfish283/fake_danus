"""The research director: turns one event plus graph context into actions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .. import config
from ..gemini_client import generate
from ..graph.graph import ResearchGraph
from .actions import ACTION_SCHEMA, Action, ActionParseError, parse_actions
from .prompts import PLANNER_PROMPT, WORKER_ROLE_BLURBS


@dataclass
class PlannerDecision:
    reasoning: str
    actions: list[Action]


class Planner:
    """One Gemini call per event, returning structured actions."""

    def __init__(self, problem: str) -> None:
        self.problem = problem
        self.calls = 0

    def build_prompt(
        self,
        *,
        graph: ResearchGraph,
        event_text: str,
        retrieval_query: str,
        focus: Iterable[str] = (),
        worker_status: str = "",
        budget_status: str = "",
        history: Sequence[str] = (),
    ) -> str:
        graph_context = graph.context_for(
            retrieval_query, limit=config.PLANNER_CONTEXT_NODES, focus=focus
        )
        roles = "\n".join(f"- {role}: {blurb}" for role, blurb in WORKER_ROLE_BLURBS.items())

        sections = [
            f"# Problem\n\n{self.problem.strip()}",
            "# Research graph (a slice; nodes not shown still exist)\n\n"
            + (graph_context or "(empty)")
            + f"\n\nGraph size: {graph.stats_line()}",
            f"# New event\n\n{event_text.strip()}",
        ]
        if history:
            sections.append("# Recent history\n\n" + "\n".join(history))
        sections.append(f"# Workers\n\n{roles}\n\n{worker_status or 'All workers idle.'}")
        if budget_status:
            sections.append(f"# Budget\n\n{budget_status}")
        sections.append(
            "# Now decide\n\n"
            "React to the new event. Record what is genuinely new, update statuses that "
            "have changed, connect related nodes, and keep idle slots busy on "
            "specific tasks. Return JSON matching the schema."
        )
        return "\n\n".join(sections)

    async def decide(
        self,
        *,
        graph: ResearchGraph,
        event_text: str,
        retrieval_query: str = "",
        focus: Iterable[str] = (),
        worker_status: str = "",
        budget_status: str = "",
        history: Sequence[str] = (),
    ) -> PlannerDecision:
        prompt = self.build_prompt(
            graph=graph,
            event_text=event_text,
            retrieval_query=retrieval_query or event_text,
            focus=focus,
            worker_status=worker_status,
            budget_status=budget_status,
            history=history,
        )

        last_error: Exception | None = None
        for attempt in range(2):
            text = await generate(
                prompt if attempt == 0 else prompt + _RETRY_SUFFIX.format(error=last_error),
                role="planner",
                model=config.PLANNER_MODEL,
                system_instruction=PLANNER_PROMPT,
                thinking_level=config.PLANNER_THINKING_LEVEL,
                max_output_tokens=config.PLANNER_MAX_OUTPUT_TOKENS,
                response_schema=ACTION_SCHEMA,
            )
            self.calls += 1
            try:
                reasoning, actions = parse_actions(text)
            except ActionParseError as exc:
                last_error = exc
                continue
            return PlannerDecision(reasoning=reasoning, actions=actions)

        raise ActionParseError(f"planner output could not be parsed twice: {last_error}")


_RETRY_SUFFIX = """

# Retry

Your previous reply could not be parsed ({error}). Return only a JSON object
with keys "reasoning" (string) and "actions" (array), matching the schema. No
markdown, no commentary outside the JSON.
"""
