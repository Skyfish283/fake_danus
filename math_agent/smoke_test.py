"""Verify every configured key and model before running the full system.

One call per role, so a bad key or an unavailable model shows up here rather
than halfway through a run.

Usage:  python -m math_agent.smoke_test
"""

from __future__ import annotations

import asyncio
import sys

from . import config
from .gemini_client import USAGE, generate, set_note_sink


async def check(role: str, *, key_role: str | None = None) -> bool:
    billed = key_role or role
    print(f"\n{role}: {config.model_status(role)}")
    print(f"  key: {config.key_status(billed)}" + (f" (via {key_role})" if key_role else ""))
    try:
        text = await generate(
            "Reply with exactly: connection ok",
            role=role,
            key_role=key_role,
            thinking_level="LOW",
            max_output_tokens=512,
        )
    except Exception as exc:  # noqa: BLE001 - this script exists to report failures
        print(f"  FAIL: {type(exc).__name__}: {exc}")
        return False

    print(f"  replied: {text!r}")
    return True


async def main() -> int:
    set_note_sink(lambda _actor, message: print(f"  note: {message}"))
    print(f"config: {config.RUN_CONFIG.path or 'built-in defaults'}")
    for warning in config.RUN_CONFIG.warnings:
        print(f"  warning: {warning}")

    roles = list(config.RUN_CONFIG.roles_in_use())
    try:
        config.require_api_keys(roles)
    except config.MissingAPIKey as exc:
        print(f"\nFAIL: {exc}")
        return 1

    results = [await check(role) for role in roles]
    checked = list(roles)
    if config.RUN_CONFIG.mode == "main":
        # Verifier has no key of its own; bill the explorer pool (flex_1).
        checked.append("verifier")
        results.append(await check("verifier", key_role="explorer"))

    print(f"\n{USAGE.summary()}")
    if all(results):
        print("OK")
        return 0
    failed = [role for role, ok in zip(checked, results) if not ok]
    print(f"FAIL: {', '.join(failed)}")
    return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
