"""Worker: construct toy examples that satisfy the assumptions and show the mechanism."""

from __future__ import annotations

from .. import config
from ..agent.prompts import TOY_EXAMPLE_PROMPT
from .base import WorkerOutcome, run_worker

ROLE = "toy_example"
SYSTEM_PROMPT = TOY_EXAMPLE_PROMPT
MODEL = config.WORKER_MODELS["explorer"]
THINKING_LEVEL = config.WORKER_THINKING_LEVELS["explorer"]


async def run(task_id: str, task: str, problem: str, context: str = "") -> WorkerOutcome:
    return await run_worker(
        task_id=task_id, role=ROLE, task=task, problem=problem, context=context
    )
