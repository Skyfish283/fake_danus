"""One Gemini call per worker, wrapped so a failure never kills the run."""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass

from .. import config
from ..agent.prompts import WORKER_PROMPTS
from ..gemini_client import generate

# Every slot is flexible: the planner must set a role on each assignment.
SPECIALIZED_SLOTS: tuple[str, ...] = ()
FLEX_SLOTS = ("flex_1", "flex_2", "flex_3", "flex_4", "flex_5", "flex_6")
WORKER_SLOTS = FLEX_SLOTS

# Prompt roles the planner can assign. `verifier` is allowed anywhere now.
PROMPT_ROLES = (
    "searcher",
    "toy_example",
    "counterexample",
    "decomposer",
    "sketcher",
    "verifier",
)

# Which run_config.toml role ([models], [thinking]) each prompt role is
# configured against. The config keeps the original explorer/mathematician/
# skeptic/verifier names so existing configs keep working; the baselines
# (arm B) also still run under those names.
PROMPT_CONFIG_ROLE = {
    "searcher": "explorer",
    "toy_example": "explorer",
    "counterexample": "skeptic",
    "decomposer": "mathematician",
    "sketcher": "mathematician",
    "verifier": "verifier",
}

# Which [api_keys] pool each prompt role bills. The verifier has no key of
# its own and bills the explorer pool.
PROMPT_KEY_ROLE = {
    "searcher": "explorer",
    "toy_example": "explorer",
    "counterexample": "skeptic",
    "decomposer": "mathematician",
    "sketcher": "mathematician",
    "verifier": "explorer",
}

# Bounds how many worker calls are in flight at once, independently of how
# many tasks the planner assigns.
_semaphore = asyncio.Semaphore(config.MAX_CONCURRENT_WORKERS)


@dataclass
class WorkerOutcome:
    """Result of one worker call, successful or not."""

    task_id: str
    role: str
    task: str
    ok: bool
    content: str = ""
    error: str = ""
    elapsed: float = 0.0
    slot: str = ""


def resolve_assignment(slot: str, requested_role: str = "") -> tuple[str | None, str]:
    """Map an ASSIGN_TASK onto a (role, error) pair.

    Every slot is flexible and requires a prompt role. Returns `(None, reason)`
    when the assignment is invalid.
    """
    slot = (slot or "").strip().lower()
    requested = (requested_role or "").strip().lower()
    if slot not in WORKER_SLOTS:
        return None, (
            f"unknown worker slot {slot!r}; expected one of {', '.join(WORKER_SLOTS)}"
        )
    if requested not in PROMPT_ROLES:
        shown = requested_role.strip() or "(empty)"
        return None, (
            f"slot {slot} needs a role ({', '.join(PROMPT_ROLES)}); got {shown!r}"
        )
    return requested, ""


def build_worker_prompt(problem: str, context: str, task: str) -> str:
    """Assemble the user-turn prompt: problem, graph slice, then the task."""
    sections = [f"# Problem\n\n{problem.strip()}"]
    if context.strip():
        sections.append(f"# Current relevant research\n\n{context.strip()}")
    sections.append(
        "# Your task\n\n"
        f"{task.strip()}\n\n"
        "Address this task specifically. Do not produce a general essay on the problem."
    )
    return "\n\n".join(sections)


async def run_worker(
    *,
    task_id: str,
    role: str,
    task: str,
    problem: str,
    context: str = "",
    slot: str = "",
) -> WorkerOutcome:
    """Run one worker to completion, returning an outcome rather than raising."""
    if role not in WORKER_PROMPTS:
        return WorkerOutcome(
            task_id=task_id,
            role=role,
            task=task,
            ok=False,
            error=f"unknown worker role {role!r}; expected one of {', '.join(PROMPT_ROLES)}",
            slot=slot,
        )

    # Billing follows the assigned role, not the slot; the explorer pool is
    # the fallback (verifier has no key of its own).
    key_role = PROMPT_KEY_ROLE[role]
    config_role = PROMPT_CONFIG_ROLE[role]
    started = time.monotonic()
    try:
        async with _semaphore:
            content = await generate(
                build_worker_prompt(problem, context, task),
                role=role,
                key_role=key_role,
                model=config.WORKER_MODELS[config_role],
                system_instruction=WORKER_PROMPTS[role],
                thinking_level=config.WORKER_THINKING_LEVELS[config_role],
                max_output_tokens=config.WORKER_MAX_OUTPUT_TOKENS,
            )
    except asyncio.CancelledError:
        raise
    except Exception as exc:  # noqa: BLE001 - reported as a task_failed event
        return WorkerOutcome(
            task_id=task_id,
            role=role,
            task=task,
            ok=False,
            error=f"{type(exc).__name__}: {exc}",
            elapsed=time.monotonic() - started,
            slot=slot,
        )

    return WorkerOutcome(
        task_id=task_id,
        role=role,
        task=task,
        ok=True,
        content=content,
        elapsed=time.monotonic() - started,
        slot=slot,
    )
