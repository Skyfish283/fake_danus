"""Worker: search math results — literature, known theorems, lateral analogies."""

from __future__ import annotations

from .. import config
from ..agent.prompts import SEARCHER_PROMPT
from .base import WorkerOutcome, run_worker

ROLE = "searcher"
SYSTEM_PROMPT = SEARCHER_PROMPT
MODEL = config.WORKER_MODELS["explorer"]
THINKING_LEVEL = config.WORKER_THINKING_LEVELS["explorer"]


async def run(task_id: str, task: str, problem: str, context: str = "") -> WorkerOutcome:
    return await run_worker(
        task_id=task_id, role=ROLE, task=task, problem=problem, context=context
    )
