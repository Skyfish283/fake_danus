"""Worker: propose materially different subgoal decomposition plans."""

from __future__ import annotations

from .. import config
from ..agent.prompts import DECOMPOSER_PROMPT
from .base import WorkerOutcome, run_worker

ROLE = "decomposer"
SYSTEM_PROMPT = DECOMPOSER_PROMPT
MODEL = config.WORKER_MODELS["mathematician"]
THINKING_LEVEL = config.WORKER_THINKING_LEVELS["mathematician"]


async def run(task_id: str, task: str, problem: str, context: str = "") -> WorkerOutcome:
    return await run_worker(
        task_id=task_id, role=ROLE, task=task, problem=problem, context=context
    )
