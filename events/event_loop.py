"""Event bus and supervisor loop.

The supervisor blocks on one event at a time and calls the planner for that
event alone. Workers and literature calls run as background asyncio tasks, so
whichever finishes first is what the planner reacts to next. There are no
rounds and no barrier that waits for every worker.
"""

from __future__ import annotations

import asyncio
import itertools
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Any

from .. import config
from ..agent.actions import Action, ActionParseError, apply_graph_action
from ..agent.planner import Planner
from ..graph.graph import ResearchGraph
from ..run_log import RunLog
from ..tools import papers as papers_tool
from ..workers.base import WORKER_SLOTS, resolve_assignment, run_worker

EVENT_TYPES = (
    "user_message",
    "worker_result",
    "task_failed",
    "task_completed",
    "search_result",
    "paper_retrieved",
    "system_idle",
)


@dataclass
class Event:
    """Something that happened and that the planner should react to."""

    type: str
    source: str = "system"
    payload: dict[str, Any] = field(default_factory=dict)
    ts: float = field(default_factory=time.time)

    def headline(self) -> str:
        if self.type == "worker_result":
            return f"{self.source} finished: {_clip(self.payload.get('task', ''), 70)}"
        if self.type == "task_failed":
            return f"{self.source} failed: {_clip(self.payload.get('error', ''), 70)}"
        if self.type == "search_result":
            return (
                f"search returned {self.payload.get('count', 0)} results for "
                f"{_clip(self.payload.get('query', ''), 60)}"
            )
        if self.type == "paper_retrieved":
            return f"paper retrieved: {_clip(self.payload.get('title', ''), 70)}"
        if self.type == "user_message":
            return "user stated the problem"
        if self.type == "system_idle":
            return "no work in flight"
        return self.type

    def render_for_planner(self) -> str:
        kind = self.type.upper()
        if self.type == "worker_result":
            slot = self.payload.get("slot")
            slot_bit = f", slot {slot}" if slot else ""
            return (
                f"{kind} from {self.source} (task {self.payload.get('task_id', '?')}{slot_bit})\n"
                f"Task was: {self.payload.get('task', '')}\n\n"
                f"{self.payload.get('content', '')}"
            )
        if self.type == "task_failed":
            slot = self.payload.get("slot")
            slot_bit = f", slot {slot}" if slot else ""
            return (
                f"{kind}: {self.source} could not complete task "
                f"{self.payload.get('task_id', '?')}{slot_bit} "
                f"({self.payload.get('task', '')}).\n"
                f"Error: {self.payload.get('error', '')}\n"
                "Decide whether to retry it, reassign it differently, or move on."
            )
        if self.type == "search_result":
            return f"{kind}\n\n{self.payload.get('text', '')}"
        if self.type == "paper_retrieved":
            return f"{kind}\n\n{self.payload.get('text', '')}"
        if self.type == "user_message":
            return (
                f"{kind}\n\n{self.payload.get('text', '')}\n\n"
                "This is the start of the research programme. Open several distinct "
                "lines of attack: give idle slots specific, different tasks with "
                "roles chosen from the work cycle, and record the initial framing "
                "in the graph."
            )
        if self.type == "system_idle":
            return (
                f"{kind}\n\nNo workers are running and nothing is queued. Either push the "
                "research forward with new tasks or searches, or FINISH with a summary if "
                "the graph already contains what a human researcher would need."
            )
        return f"{kind}\n\n{self.payload}"

    def retrieval_query(self) -> str:
        parts = [
            str(self.payload.get("task", "")),
            str(self.payload.get("query", "")),
            str(self.payload.get("title", "")),
            str(self.payload.get("content", ""))[:2000],
            str(self.payload.get("text", ""))[:2000],
        ]
        return " ".join(part for part in parts if part)

    def to_record(self) -> dict[str, Any]:
        payload = dict(self.payload)
        for key in ("content", "text"):
            if key in payload and isinstance(payload[key], str):
                payload[key] = payload[key]
        return {"event": self.type, "source": self.source, "payload": payload}


class EventBus:
    """Thin wrapper over asyncio.Queue, so producers do not touch the loop."""

    def __init__(self) -> None:
        self._queue: asyncio.Queue[Event] = asyncio.Queue()

    async def put(self, event: Event) -> None:
        await self._queue.put(event)

    def put_nowait(self, event: Event) -> None:
        self._queue.put_nowait(event)

    async def get(self) -> Event:
        return await self._queue.get()

    def empty(self) -> bool:
        return self._queue.empty()

    def qsize(self) -> int:
        return self._queue.qsize()


@dataclass
class PendingTask:
    task_id: str
    kind: str
    role: str
    description: str
    task: asyncio.Task
    started: float = field(default_factory=time.monotonic)
    slot: str = ""


class Supervisor:
    """Owns the graph, the event bus, and everything currently in flight."""

    def __init__(
        self,
        *,
        problem: str,
        graph: ResearchGraph,
        planner: Planner,
        log: RunLog,
        max_planner_calls: int = config.MAX_PLANNER_CALLS,
        max_worker_calls: int = config.MAX_WORKER_CALLS,
        max_seconds: float = config.MAX_WALL_CLOCK_SECONDS,
    ) -> None:
        self.problem = problem
        self.graph = graph
        self.planner = planner
        self.log = log
        self.bus = EventBus()

        self.pending: dict[str, PendingTask] = {}
        self.planner_lock = asyncio.Lock()
        self.history: deque[str] = deque(maxlen=config.RECENT_EVENT_TAIL)
        self._ids = itertools.count(1)

        self.finished = False
        self.finish_reason = ""
        self.final_summary = ""
        # Metadata from search results, so GET_PAPER need not re-fetch it.
        self.search_cache: dict[str, papers_tool.Paper] = {}

        self.planner_calls = 0
        self.worker_calls = 0
        self.max_planner_calls = max_planner_calls
        self.max_worker_calls = max_worker_calls
        self.max_seconds = max_seconds
        self.started = time.monotonic()
        self._idle_offered = False

    # -- budget -------------------------------------------------------------

    @property
    def elapsed(self) -> float:
        return time.monotonic() - self.started

    def budget_exhausted(self) -> str:
        if self.planner_calls >= self.max_planner_calls:
            return f"planner call cap reached ({self.max_planner_calls})"
        if self.elapsed >= self.max_seconds:
            return f"time cap reached ({self.max_seconds:.0f}s)"
        return ""

    def budget_status(self) -> str:
        return (
            f"Planner calls: {self.planner_calls}/{self.max_planner_calls}. "
            f"Worker calls: {self.worker_calls}/{self.max_worker_calls}. "
            f"Elapsed: {self.elapsed:.0f}s of {self.max_seconds:.0f}s. "
            "When the budget runs low, consolidate and FINISH with a full summary."
        )

    def worker_status(self) -> str:
        busy_by_slot = {
            p.slot: p for p in self.pending.values() if p.kind == "worker" and p.slot
        }
        lines = []
        for slot in WORKER_SLOTS:
            pending = busy_by_slot.get(slot)
            if pending:
                lines.append(
                    f"- {slot} busy as {pending.role} [{pending.task_id}]: "
                    f"{_clip(pending.description, 100)} "
                    f"({time.monotonic() - pending.started:.0f}s so far)"
                )
            else:
                lines.append(f"- {slot} idle")
        others = [p for p in self.pending.values() if p.kind != "worker"]
        if others:
            lines.append("Also running:")
            for pending in others:
                lines.append(
                    f"- {pending.role} [{pending.task_id}]: "
                    f"{_clip(pending.description, 100)} "
                    f"({time.monotonic() - pending.started:.0f}s so far)"
                )
        lines.append("Do not assign a slot that is already busy.")
        return "Worker slots:\n" + "\n".join(lines)

    # -- main loop ----------------------------------------------------------

    async def run(self, seed: Event) -> None:
        await self.bus.put(seed)

        while not self.finished:
            reason = self.budget_exhausted()
            if reason:
                self.finish_reason = reason
                self.log.line("System", f"stopping: {reason}")
                break

            if self.bus.empty() and not self.pending:
                if self._idle_offered:
                    self.finish_reason = self.finish_reason or "no work left and planner had nothing more to add"
                    self.log.line("System", "idle with nothing left to do; stopping")
                    break
                self._idle_offered = True
                await self.bus.put(Event(type="system_idle"))

            try:
                # The timeout doubles as a watchdog so the time cap is noticed
                # even while every worker is still thinking.
                event = await asyncio.wait_for(self.bus.get(), timeout=5)
            except asyncio.TimeoutError:
                continue

            await self.handle(event)

        await self.shutdown()

    async def handle(self, event: Event) -> None:
        if event.type != "system_idle":
            self._idle_offered = False

        self.log.record_event(event.to_record())
        if event.type == "worker_result":
            self.log.line(event.source, f"result ({len(event.payload.get('content', ''))} chars)")
            self.log.block(f"{event.source} result", event.payload.get("content", ""))
        elif event.type == "task_failed":
            self.log.error(f"{event.source}: {event.payload.get('error', '')}")
        elif event.type in ("search_result", "paper_retrieved"):
            self.log.line("Papers", event.headline())
        else:
            self.log.line("System", event.headline())

        async with self.planner_lock:
            reason = self.budget_exhausted()
            if reason:
                self.finish_reason = reason
                self.finished = True
                return
            try:
                decision = await self.planner.decide(
                    graph=self.graph,
                    event_text=event.render_for_planner(),
                    retrieval_query=event.retrieval_query(),
                    focus=event.payload.get("focus_nodes", ()) or (),
                    worker_status=self.worker_status(),
                    budget_status=self.budget_status(),
                    history=list(self.history),
                )
            except ActionParseError as exc:
                self.log.error(f"planner output unusable, skipping this event: {exc}")
                return
            except Exception as exc:  # noqa: BLE001 - one bad call must not end the run
                self.log.error(f"planner call failed: {type(exc).__name__}: {exc}")
                return
            finally:
                # Counts real API calls, so a retried decision costs two.
                self.planner_calls = max(self.planner_calls, self.planner.calls)

        if decision.reasoning:
            self.log.line("Gemini", decision.reasoning)
        self.history.append(f"[{time.strftime('%H:%M:%S')}] {event.headline()}")

        await self.execute(decision.actions)

    # -- action execution ---------------------------------------------------

    async def execute(self, actions: list[Action]) -> None:
        for action in actions:
            if self.finished:
                return
            try:
                await self.execute_one(action)
            except Exception as exc:  # noqa: BLE001 - never let one action end the run
                self.log.error(f"action {action.type} failed: {type(exc).__name__}: {exc}")

    async def execute_one(self, action: Action) -> None:
        if action.type in ("ADD_NODE", "UPDATE_NODE", "ADD_EDGE"):
            result = apply_graph_action(self.graph, action)
            self.log.line("Gemini", f"graph: {result}")
            self.log.record_event({"event": "graph_action", "action": action.raw, "result": result})
            return

        if action.type == "ASSIGN_TASK":
            self.assign_task(action)
            return

        if action.type == "CANCEL_TASK":
            self.cancel_task(str(action.get("task_id", "id")))
            return

        if action.type == "SEARCH_PAPERS":
            self.spawn_search(action)
            return

        if action.type == "GET_PAPER":
            self.spawn_paper_fetch(action)
            return

        if action.type == "FINISH":
            self.final_summary = str(action.get("summary", default=""))
            self.finish_reason = self.finish_reason or "planner returned FINISH"
            self.finished = True
            self.log.line("Gemini", "FINISH")
            return

    def _new_task_id(self, prefix: str) -> str:
        return f"{prefix}_{next(self._ids)}"

    def _register(self, pending: PendingTask) -> None:
        self.pending[pending.task_id] = pending
        # Safety net for cancellation and crashes; the normal path deregisters
        # in _emit_done, because done callbacks only run once the loop yields.
        pending.task.add_done_callback(lambda _t, tid=pending.task_id: self.pending.pop(tid, None))
        self._idle_offered = False

    async def _emit_done(self, task_id: str, event: Event) -> None:
        """Retire a finished task and publish its result."""
        self.pending.pop(task_id, None)
        await self.bus.put(event)

    # -- dispatching actions ------------------------------------------------

    def assign_task(self, action: Action) -> None:
        slot = str(action.get("worker", default="flex_1")).strip().lower()
        requested_role = str(action.get("role", default="")).strip().lower()
        task_text = str(action.get("task")).strip()
        if not task_text:
            self.log.error("ASSIGN_TASK skipped: empty task")
            return
        role, error = resolve_assignment(slot, requested_role)
        if error:
            self.log.error(f"ASSIGN_TASK skipped: {error}")
            return
        if self._slot_busy(slot):
            self.log.line("System", f"ASSIGN_TASK skipped: slot {slot} is already busy")
            return
        if self.worker_calls >= self.max_worker_calls:
            self.log.line("System", f"worker cap reached ({self.max_worker_calls}); task not assigned")
            return
        if len(self.pending) >= config.MAX_CONCURRENT_WORKERS * 2:
            self.log.line("System", "too many tasks in flight; task not assigned")
            return

        focus = list(action.get("focus_nodes", default=[]) or [])
        context = self.graph.context_for(
            task_text, limit=config.WORKER_CONTEXT_NODES, focus=focus
        )
        task_id = self._new_task_id("task")
        self.worker_calls += 1
        self.log.line("Gemini", f"-> {slot} as {role} [{task_id}] {_clip(task_text, 110)}")

        coro = self._run_worker_task(
            task_id=task_id,
            slot=slot,
            role=role,
            task=task_text,
            context=context,
            focus=focus,
        )
        self._register(
            PendingTask(
                task_id=task_id,
                kind="worker",
                role=role,
                slot=slot,
                description=task_text,
                task=asyncio.create_task(coro, name=task_id),
            )
        )

    def _slot_busy(self, slot: str) -> bool:
        return any(p.kind == "worker" and p.slot == slot for p in self.pending.values())

    async def _run_worker_task(
        self,
        *,
        task_id: str,
        slot: str,
        role: str,
        task: str,
        context: str,
        focus: list[str],
    ) -> None:
        outcome = await run_worker(
            task_id=task_id,
            role=role,
            slot=slot,
            task=task,
            problem=self.problem,
            context=context,
        )
        payload = {
            "task_id": task_id,
            "task": task,
            "slot": slot,
            "focus_nodes": focus,
        }
        if outcome.ok:
            event = Event(
                type="worker_result",
                source=role,
                payload={
                    **payload,
                    "content": outcome.content,
                    "elapsed": round(outcome.elapsed, 1),
                },
            )
        else:
            event = Event(
                type="task_failed",
                source=role,
                payload={**payload, "error": outcome.error},
            )
        await self._emit_done(task_id, event)

    def cancel_task(self, task_id: str) -> None:
        pending = self.pending.pop(task_id, None)
        if pending is None:
            self.log.line("System", f"CANCEL_TASK: no running task {task_id}")
            return
        pending.task.cancel()
        self.log.line("System", f"cancelled {task_id} ({pending.slot or pending.role})")

    def spawn_search(self, action: Action) -> None:
        query = str(action.get("query")).strip()
        if not query:
            self.log.error("SEARCH_PAPERS skipped: empty query")
            return
        source = str(action.get("search_source", "source", default="openalex")).strip().lower()
        task_id = self._new_task_id("search")
        self.log.line("Gemini", f"-> SEARCH_PAPERS [{source}] {_clip(query, 100)}")
        self._register(
            PendingTask(
                task_id=task_id,
                kind="search",
                role="literature",
                description=f"search: {query}",
                task=asyncio.create_task(self._run_search(task_id, query, source), name=task_id),
            )
        )

    async def _run_search(self, task_id: str, query: str, source: str) -> None:
        try:
            results, used, errors = await papers_tool.search_papers(query, source)
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # noqa: BLE001 - reported to the planner
            await self._emit_done(
                task_id,
                Event(
                    type="task_failed",
                    source="literature",
                    payload={"task_id": task_id, "task": f"search {query!r}", "error": str(exc)},
                ),
            )
            return

        for paper in results:
            self.search_cache[paper.id] = paper
        text = papers_tool.render_results(results, query, used)
        if errors and not results:
            text += "\n\nBackend notes: " + "; ".join(errors)
        await self._emit_done(
            task_id,
            Event(
                type="search_result",
                source="literature",
                payload={
                    "task_id": task_id,
                    "query": query,
                    "source": used,
                    "count": len(results),
                    "text": text,
                    "papers": [p.to_dict() for p in results],
                },
            ),
        )

    def spawn_paper_fetch(self, action: Action) -> None:
        paper_id = str(action.get("paper_id", "id")).strip()
        if not paper_id:
            self.log.error("GET_PAPER skipped: empty paper_id")
            return
        task_id = self._new_task_id("paper")
        self.log.line("Gemini", f"-> GET_PAPER {paper_id}")
        self._register(
            PendingTask(
                task_id=task_id,
                kind="paper",
                role="literature",
                description=f"paper: {paper_id}",
                task=asyncio.create_task(self._run_paper_fetch(task_id, paper_id), name=task_id),
            )
        )

    async def _run_paper_fetch(self, task_id: str, paper_id: str) -> None:
        try:
            paper, text, note = await papers_tool.get_paper(
                paper_id, self.search_cache.get(paper_id)
            )
        except asyncio.CancelledError:
            raise
        except Exception as exc:  # noqa: BLE001 - reported to the planner
            await self._emit_done(
                task_id,
                Event(
                    type="task_failed",
                    source="literature",
                    payload={
                        "task_id": task_id,
                        "task": f"retrieve {paper_id}",
                        "error": f"{type(exc).__name__}: {exc}",
                    },
                ),
            )
            return

        await self._emit_done(
            task_id,
            Event(
                type="paper_retrieved",
                source="literature",
                payload={
                    "task_id": task_id,
                    "paper_id": paper.id,
                    "title": paper.title,
                    "note": note,
                    "text": papers_tool.render_paper(paper, text, note),
                    "meta": paper.to_dict(),
                },
            ),
        )

    # -- shutdown -----------------------------------------------------------

    async def shutdown(self) -> None:
        """Cancel anything still running and wait for it to unwind."""
        if not self.pending:
            return
        self.log.line("System", f"cancelling {len(self.pending)} task(s) still in flight")
        tasks = [p.task for p in list(self.pending.values())]
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        self.pending.clear()


def _clip(text: Any, limit: int) -> str:
    text = str(text).replace("\n", " ").strip()
    return text if len(text) <= limit else text[: limit - 3] + "..."
