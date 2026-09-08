"""Worker: falsify claims by constructing objects that break the conclusion."""

from __future__ import annotations

from .. import config
from ..agent.prompts import COUNTEREXAMPLE_PROMPT
from .base import WorkerOutcome, run_worker

ROLE = "counterexample"
SYSTEM_PROMPT = COUNTEREXAMPLE_PROMPT
MODEL = config.WORKER_MODELS["skeptic"]
THINKING_LEVEL = config.WORKER_THINKING_LEVELS["skeptic"]


async def run(task_id: str, task: str, problem: str, context: str = "") -> WorkerOutcome:
    return await run_worker(
        task_id=task_id, role=ROLE, task=task, problem=problem, context=context
    )
