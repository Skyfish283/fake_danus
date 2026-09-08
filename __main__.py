"""Run whatever run_config.toml says, with no command-line arguments.

    cd C:\\Users\\samfe\\OneDrive\\Desktop
    python -m math_agent

`[run] mode` picks the entry point: the full agentic system, or one of the
baseline arms. Use `python -m math_agent.main --help` for one-off overrides.
"""

from __future__ import annotations

import asyncio
import sys

from .run_config import ConfigError


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv:
        print(
            "python -m math_agent takes no arguments: edit run_config.toml instead.\n"
            "For one-off overrides use python -m math_agent.main or "
            "python -m math_agent.baselines.",
            file=sys.stderr,
        )
        return 2

    try:
        # Importing config parses and validates run_config.toml.
        from . import config
    except ConfigError as exc:
        print(exc, file=sys.stderr)
        return 1

    try:
        options = config.options_from(config.RUN_CONFIG)
    except ConfigError as exc:
        print(exc, file=sys.stderr)
        return 1

    if options.mode == "main":
        from .main import run
    else:
        from .baselines import run

    try:
        return asyncio.run(run(options))
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
