"""Worker role: check a claimed lemma, theorem, or proof. Flex slots only."""

from __future__ import annotations

from .. import config
from ..agent.prompts import VERIFIER_PROMPT
from .base import WorkerOutcome, run_worker

ROLE = "verifier"
SYSTEM_PROMPT = VERIFIER_PROMPT
MODEL = config.WORKER_MODELS[ROLE]
THINKING_LEVEL = config.WORKER_THINKING_LEVELS[ROLE]


async def run(task_id: str, task: str, problem: str, context: str = "") -> WorkerOutcome:
    return await run_worker(
        task_id=task_id, role=ROLE, task=task, problem=problem, context=context
    )
