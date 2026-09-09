"""Comparison arms for the experiment: does the architecture actually help?

Arm A: one Gemini call.
Arm B: the original three worker roles, run once each in parallel and
       synthesised, but with no research graph, no literature tools and no
       event loop - a fixed pipeline rather than an agent.
Arm C is the full system: `python -m math_agent.main`.

Keep the models in run_config.toml identical across arms, so any difference is
architectural rather than a difference in raw model strength.

    python -m math_agent          # with [run] mode = "baselines_both"
    python -m math_agent.baselines "problem" --arm both
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from . import config
from .agent.prompts import SHARED_WORKER_PREAMBLE
from .config import RunOptions
from .gemini_client import USAGE, generate, set_note_sink
from .run_log import RunLog, new_run_dir
from .workers.base import build_worker_prompt

BASELINE_A_PROMPT = """\
You are a research mathematician advising a colleague on a hard problem.

Give them approaches to this mathematical problem: distinct lines of attack,
the standard machinery that might apply, the obstacles each route faces, and
any literature worth reading. You are not expected to prove anything. Be
concrete and mathematical, name specific theorems and techniques, and be
explicit about what you are unsure of.
"""

# Arm B keeps the original three worker roles (the pre-Danus prompt set) so
# the comparison arm stays a fixed pipeline rather than tracking the live
# worker roster.
ARM_B_ROLES = ("explorer", "mathematician", "skeptic")

ARM_B_PROMPTS = {
    "explorer": SHARED_WORKER_PREAMBLE
    + """
YOUR ROLE: EXPLORER.

Generate unconventional or alternative approaches. You are the source of
lateral thinking in this system, so deliberately avoid the single most obvious
textbook attack unless you can add a twist to it.

Look for:
- different mathematical frameworks the problem could be recast in
  (probabilistic, geometric, algebraic, combinatorial, analytic, categorical,
  computational, information-theoretic)
- transformations, changes of variable, dualities, compactifications,
  discretisations, continuum limits, generating functions, integral transforms
- analogous problems in other fields whose solution technique might transfer
- special cases, degenerate cases and toy models that might reveal structure
- unexpected connections between apparently unrelated areas

GROUND YOUR IDEAS:
If you propose a new framework, transformation, or analogy, immediately test
it by applying it to the trivial, 1D, or degenerate version of the problem.
Does it reduce correctly? Does the analogy hold up in the simplest case?
Speculative is fine, but label speculation as speculation, and show the
trivial case calculation.
""",
    "mathematician": SHARED_WORKER_PREAMBLE
    + """
YOUR ROLE: MATHEMATICIAN.

Investigate the standard machinery that might attack the current target. You
are the source of rigour and established technique in this system.

Look for:
- known theorems that apply, with their exact hypotheses
- standard proof techniques for problems of this shape
- reductions to better-understood problems
- lemmas that would suffice, and how hard each looks to prove
- the assumptions any proposed route silently requires
- connections to existing theory and where this problem sits in the literature

Where a route needs a lemma, state the lemma precisely enough that someone
could try to prove it. Where a theorem nearly applies but not quite, say
precisely which hypothesis fails.

ATTEMPTING PROOFS:
While you are not a formal automated theorem prover, if your assigned task
involves a specific, bounded, or computational lemma that you judge to be
tractable, YOU SHOULD ATTEMPT THE PROOF.

Lay out the argument or calculation step-by-step. Do not just say "a standard
argument shows..."—do the actual algebra or computation. If the calculation
is straightforward, execute it completely. If you hit a snag or realize an
assumption is missing mid-proof, document exactly where and why it fails.
""",
    "skeptic": SHARED_WORKER_PREAMBLE
    + """
YOUR ROLE: SKEPTIC.

Attack the current approaches. You are adversarial, but you are a researcher,
not a formal verifier: your job is to produce useful counter-ideas, not a
verdict.

Ask:
- What could go wrong with this approach?
- Which assumption is missing or unstated?
- Can you construct a counterexample, or a family of near-counterexamples that
  shows the approach cannot work as stated?
- Is a proposed theorem actually applicable, or does a hypothesis fail?
- Which step is least convincing, and why exactly?
- Is this branch likely a dead end, and what evidence would settle that?

BE CONCRETE:
Do not just argue in the abstract. If you suspect an approach fails, test it
against a trivial 1D case, a degenerate case, or a simple toy model. Attempt
to actually construct a concrete counterexample by computing the specific
values or boundary conditions where the proposed lemma or inequality breaks
down.

Be specific: "the argument fails when the measure is not tight, as seen in
[specific toy model]" is useful, "this seems hand-wavy" is not. If an
approach survives your attack, say so clearly and say what would make it
fully convincing. Under Findings, put your strongest objections or
counterexamples; under Obstacles, put what would have to be repaired.
""",
}

# Arm B's workers get one generic task each, because the point of this arm is
# that nothing coordinates them.
ARM_B_TASKS = {
    "explorer": (
        "Generate distinct, unconventional approaches to this problem: alternative "
        "frameworks, transformations, analogous problems, and unexpected connections."
    ),
    "mathematician": (
        "Identify the standard machinery that might attack this problem: known theorems "
        "with their hypotheses, proof techniques, reductions, and lemmas that would suffice."
    ),
    "skeptic": (
        "Attack the obvious approaches to this problem: what goes wrong, which assumptions "
        "are missing, where counterexamples might live, and which routes look like dead ends."
    ),
}

ARM_B_SYNTHESIS = """\
You are a research mathematician consolidating three independent reports on the
same problem into advice for a human researcher.

Produce: the most promising directions, the obstacles each faces, anything the
reports disagree about, and open questions worth pursuing. Do not invent new
results. Be explicit about what is uncertain.
"""


async def arm_a(problem: str, log: RunLog) -> str:
    log.line("System", "Baseline A: one Gemini call")
    text = await generate(
        f"# Problem\n\n{problem}\n\nGive approaches to this problem.",
        role="baseline_a",
        model=config.BASELINE_MODEL,
        system_instruction=BASELINE_A_PROMPT,
        thinking_level=config.BASELINE_THINKING_LEVEL,
        max_output_tokens=config.PLANNER_MAX_OUTPUT_TOKENS,
    )
    log.block("baseline A", text)
    return f"# Baseline A: single Gemini call\n\n## Problem\n\n{problem}\n\n## Response\n\n{text}\n"


async def _arm_b_worker(role: str, problem: str, log: RunLog) -> tuple[str, str]:
    try:
        text = await generate(
            build_worker_prompt(problem, "", ARM_B_TASKS[role]),
            role=f"baseline_b_{role}",
            model=config.WORKER_MODELS[role],
            system_instruction=ARM_B_PROMPTS[role],
            thinking_level=config.WORKER_THINKING_LEVELS[role],
            max_output_tokens=config.WORKER_MAX_OUTPUT_TOKENS,
        )
    except Exception as exc:  # noqa: BLE001 - one arm failing should not lose the rest
        text = f"(failed: {type(exc).__name__}: {exc})"
    log.line(role, "done")
    return role, text


async def arm_b(problem: str, log: RunLog) -> str:
    log.line("System", "Baseline B: three workers in parallel, no graph, no event loop")
    # Waits for all three: the fixed pipeline the full system deliberately avoids.
    results = dict(await asyncio.gather(*(_arm_b_worker(r, problem, log) for r in ARM_B_ROLES)))

    reports = "\n\n".join(
        f"## Report from the {role}\n\n{results[role]}" for role in ARM_B_ROLES
    )
    log.line("System", "synthesising")
    synthesis = await generate(
        f"# Problem\n\n{problem}\n\n# Reports\n\n{reports}\n\n"
        "Consolidate these into advice for the human researcher.",
        role="baseline_b_synthesis",
        model=config.BASELINE_MODEL,
        system_instruction=ARM_B_SYNTHESIS,
        thinking_level=config.BASELINE_THINKING_LEVEL,
        max_output_tokens=config.PLANNER_MAX_OUTPUT_TOKENS,
    )
    log.block("baseline B synthesis", synthesis)
    return (
        f"# Baseline B: three workers, no graph, no event loop\n\n"
        f"## Problem\n\n{problem}\n\n## Synthesis\n\n{synthesis}\n\n{reports}\n"
    )


_MODES = {"A": "baseline_a", "B": "baseline_b", "both": "baselines_both"}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m math_agent.baselines",
        description=(
            "Run the comparison baselines for the same problem. Defaults come "
            f"from {config.CONFIG_PATH.name}; every flag is an override."
        ),
    )
    parser.add_argument("problem", nargs="?", help="The mathematical problem.")
    parser.add_argument("--file", "-f", help="Read the problem from a text file.")
    parser.add_argument("--arm", choices=("A", "B", "both"))
    return parser.parse_args(argv)


def options_from_args(args: argparse.Namespace) -> RunOptions:
    """Start from the config file, then apply whatever the flags overrode."""
    options = config.options_from(config.RUN_CONFIG)
    if args.arm:
        options.mode = _MODES[args.arm]
    elif options.mode == "main":
        # `baselines.py` was invoked directly, so a config set to the full
        # system says nothing about which arm to run.
        options.mode = "baselines_both"

    if args.file:
        options.problem = Path(args.file).read_text(encoding="utf-8").strip()
    elif args.problem:
        options.problem = args.problem.strip()
    elif not options.problem:
        options.problem = input("Mathematical problem: ").strip()
    return options


async def run(options: RunOptions) -> int:
    roles = ("baseline",) if options.mode == "baseline_a" else ("baseline",) + ARM_B_ROLES
    try:
        config.require_api_keys(roles)
    except config.MissingAPIKey as exc:
        print(exc, file=sys.stderr)
        return 1

    if not options.problem:
        print("No problem given. Set [run] problem in run_config.toml.", file=sys.stderr)
        return 1

    run_dir = new_run_dir(config.RUNS_DIR, f"baseline-{options.arm}")
    log = RunLog(run_dir)
    set_note_sink(log.line)
    log.rule(f"Baselines {options.arm}")
    log.line("System", f"run directory: {run_dir}")
    log.write_config(config.render_redacted_toml(config.RUN_CONFIG, options))
    for warning in config.RUN_CONFIG.warnings:
        log.line("System", f"config warning: {warning}")
    for line in config.banner_lines(roles):
        log.line("System", line)

    outputs: list[str] = []
    try:
        for arm in options.arms:
            text = await (
                arm_a(options.problem, log) if arm == "A" else arm_b(options.problem, log)
            )
            (run_dir / f"baseline_{arm}.md").write_text(text, encoding="utf-8")
            outputs.append(text)
    finally:
        log.write_summary("\n\n---\n\n".join(outputs))
        log.line("System", USAGE.summary())
        log.line("System", f"written to {run_dir}")
        set_note_sink(None)
        log.close()
    return 0


def main(argv: list[str] | None = None) -> int:
    try:
        options = options_from_args(parse_args(argv))
    except config.ConfigError as exc:
        print(exc, file=sys.stderr)
        return 1
    try:
        return asyncio.run(run(options))
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
