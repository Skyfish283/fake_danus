"""One Gemini call per worker, wrapped so a failure never kills the run.

Now supports autonomous multi-turn execution: workers receive a subproblem,
create their own plan, select skills iteratively, and submit consolidated results.
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field

from .. import config
from ..agent.prompts import WORKER_PROMPTS, AUTONOMOUS_WORKER_SYSTEM_PROMPT
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
# configured against. All autonomous worker skills share the single "worker" role.
PROMPT_CONFIG_ROLE = {
    "searcher": "worker",
    "toy_example": "worker",
    "counterexample": "worker",
    "decomposer": "worker",
    "sketcher": "worker",
    "verifier": "worker",
}

# Which [api_keys] pool each prompt role bills. All autonomous workers share
# the single "worker" key pool.
PROMPT_KEY_ROLE = {
    "searcher": "worker",
    "toy_example": "worker",
    "counterexample": "worker",
    "decomposer": "worker",
    "sketcher": "worker",
    "verifier": "worker",
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


@dataclass
class SkillCall:
    """Records one skill invocation during autonomous worker execution."""
    skill: str
    input_task: str
    output: str
    elapsed: float = 0.0


@dataclass
class AutonomousWorkerResult:
    """Result of autonomous worker execution with multiple skill calls."""
    task_id: str
    slot: str
    initial_task: str
    final_result: str
    skill_calls: list[SkillCall] = field(default_factory=list)
    total_elapsed: float = 0.0
    error: str = ""


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


def build_autonomous_worker_prompt(
    problem: str, context: str, task: str, progress_history: list[str]
) -> str:
    """Build prompt for autonomous worker with progress tracking."""
    sections = [f"# Problem\n\n{problem.strip()}"]
    if context.strip():
        sections.append(f"# Current relevant research\n\n{context.strip()}")
    
    sections.append(f"# Your subtask\n\n{task.strip()}")
    
    if progress_history:
        sections.append("# Progress so far\n\n" + "\n\n".join(progress_history))
    
    sections.append(
        "\n\nDecide your next action: continue with a skill call, or complete the task."
    )
    return "\n\n".join(sections)


async def run_autonomous_worker(
    *,
    task_id: str,
    slot: str,
    task: str,
    problem: str,
    context: str = "",
    max_iterations: int = 5,
) -> AutonomousWorkerResult:
    """Run an autonomous worker that iteratively selects skills and executes them.
    
    The worker:
    1. Receives the initial task
    2. Decides which skill to use (or completes if done)
    3. Executes the chosen skill
    4. Reviews progress and repeats until complete or max iterations
    
    Returns consolidated results for the planner.
    """
    started = time.monotonic()
    skill_calls: list[SkillCall] = []
    progress_history: list[str] = []
    
    try:
        async with _semaphore:
            for iteration in range(max_iterations):
                # Build prompt with current progress
                prompt = build_autonomous_worker_prompt(
                    problem=problem,
                    context=context,
                    task=task,
                    progress_history=progress_history,
                )
                
                # Get worker's decision
                decision_text = await generate(
                    prompt,
                    role="searcher",  # Use worker key pool for autonomous workers
                    key_role="worker",
                    model=config.WORKER_MODELS["worker"],
                    system_instruction=AUTONOMOUS_WORKER_SYSTEM_PROMPT,
                    thinking_level=config.WORKER_THINKING_LEVELS["worker"],
                    max_output_tokens=config.WORKER_MAX_OUTPUT_TOKENS,
                )
                
                # Parse decision (simple JSON extraction)
                import json
                try:
                    decision = json.loads(decision_text)
                except json.JSONDecodeError:
                    # Try to extract JSON from text
                    import re
                    match = re.search(r'\\{[^}]+\\}', decision_text, re.DOTALL)
                    if match:
                        decision = json.loads(match.group())
                    else:
                        raise ValueError("Could not parse decision JSON")
                
                if decision.get("decision") == "complete":
                    # Worker is done, return consolidated result
                    return AutonomousWorkerResult(
                        task_id=task_id,
                        slot=slot,
                        initial_task=task,
                        final_result=decision.get("final_result", decision_text),
                        skill_calls=skill_calls,
                        total_elapsed=time.monotonic() - started,
                    )
                
                # Continue: execute the chosen skill
                skill_choice = decision.get("skill_choice")
                skill_input = decision.get("skill_input")
                
                if not skill_choice or not skill_input:
                    progress_history.append(
                        f"Iteration {iteration + 1}: Invalid decision (missing skill_choice or skill_input)"
                    )
                    continue
                
                if skill_choice not in WORKER_PROMPTS:
                    progress_history.append(
                        f"Iteration {iteration + 1}: Unknown skill {skill_choice!r}"
                    )
                    continue
                
                # Execute the skill
                skill_started = time.monotonic()
                try:
                    skill_output = await generate(
                        build_worker_prompt(problem, context, skill_input),
                        role=skill_choice,
                        key_role=PROMPT_KEY_ROLE[skill_choice],
                        model=config.WORKER_MODELS[PROMPT_CONFIG_ROLE[skill_choice]],
                        system_instruction=WORKER_PROMPTS[skill_choice],
                        thinking_level=config.WORKER_THINKING_LEVELS[PROMPT_CONFIG_ROLE[skill_choice]],
                        max_output_tokens=config.WORKER_MAX_OUTPUT_TOKENS,
                    )
                    
                    skill_elapsed = time.monotonic() - skill_started
                    skill_calls.append(SkillCall(
                        skill=skill_choice,
                        input_task=skill_input,
                        output=skill_output,
                        elapsed=skill_elapsed,
                    ))
                    progress_history.append(
                        f"Iteration {iteration + 1}: Used {skill_choice}\nInput: {skill_input}\nOutput: {skill_output[:500]}..."
                    )
                    
                except Exception as exc:
                    progress_history.append(
                        f"Iteration {iteration + 1}: Skill {skill_choice} failed: {type(exc).__name__}: {exc}"
                    )
            
            # Max iterations reached without completion
            return AutonomousWorkerResult(
                task_id=task_id,
                slot=slot,
                initial_task=task,
                final_result="Max iterations reached. Progress summary:\n\n" + "\n\n".join(progress_history),
                skill_calls=skill_calls,
                total_elapsed=time.monotonic() - started,
            )
            
    except asyncio.CancelledError:
        raise
    except Exception as exc:
        return AutonomousWorkerResult(
            task_id=task_id,
            slot=slot,
            initial_task=task,
            final_result="",
            skill_calls=skill_calls,
            total_elapsed=time.monotonic() - started,
            error=f"{type(exc).__name__}: {exc}",
        )
