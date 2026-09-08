"""Worker: attempt proof sketches and simple calculations for plans and subgoals."""

from __future__ import annotations

from .. import config
from ..agent.prompts import SKETCHER_PROMPT
from .base import WorkerOutcome, run_worker

ROLE = "sketcher"
SYSTEM_PROMPT = SKETCHER_PROMPT
MODEL = config.WORKER_MODELS["mathematician"]
THINKING_LEVEL = config.WORKER_THINKING_LEVELS["mathematician"]


async def run(task_id: str, task: str, problem: str, context: str = "") -> WorkerOutcome:
    return await run_worker(
        task_id=task_id, role=ROLE, task=task, problem=problem, context=context
    )
