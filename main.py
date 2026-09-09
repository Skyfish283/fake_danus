"""Entry point for the agentic mathematical research system.

Normally there is nothing to type: `python -m math_agent` reads run_config.toml.
The flags below stay available as one-off overrides of that file.

    python -m math_agent.main
    python -m math_agent.main "your mathematical problem"
    python -m math_agent.main --file problem.txt
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

from . import config
from .agent.planner import Planner
from .config import RunOptions
from .events.event_loop import Event, Supervisor
from .gemini_client import USAGE, set_note_sink
from .graph.graph import ResearchGraph
from .graph.storage import attach_autosave, load_graph
from .run_log import RunLog, new_run_dir
from .viewer import start_viewer

# Model roles the full system calls. API keys are shared pool-wide, so this
# only selects which banner lines and model choices to show.
MAIN_ROLES = ("planner", "worker")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m math_agent.main",
        description=(
            "Agentic mathematical research assistant (idea generation, not proving). "
            f"Defaults come from {config.CONFIG_PATH.name}; every flag is an override."
        ),
    )
    parser.add_argument("problem", nargs="?", help="The mathematical problem to research.")
    parser.add_argument("--file", "-f", help="Read the problem from a text file instead.")
    parser.add_argument("--resume", help="Continue from an existing run directory's graph.json.")
    parser.add_argument("--tag", default="", help="Label appended to the run directory name.")
    parser.add_argument(
        "--max-planner-calls", type=int,
        help=f"Cap on planner calls (config: {config.MAX_PLANNER_CALLS}).",
    )
    parser.add_argument(
        "--max-worker-calls", type=int,
        help=f"Cap on worker calls (config: {config.MAX_WORKER_CALLS}).",
    )
    parser.add_argument(
        "--max-seconds", type=float,
        help=f"Wall-clock cap in seconds (config: {config.MAX_WALL_CLOCK_SECONDS:.0f}).",
    )
    return parser.parse_args(argv)


def options_from_args(args: argparse.Namespace) -> RunOptions:
    """Start from the config file, then apply whatever the flags overrode."""
    options = config.options_from(config.RUN_CONFIG)
    options.mode = "main"
    if args.tag:
        options.tag = args.tag
    if args.resume:
        options.resume = args.resume
    if args.max_planner_calls is not None:
        options.max_planner_calls = args.max_planner_calls
    if args.max_worker_calls is not None:
        options.max_worker_calls = args.max_worker_calls
    if args.max_seconds is not None:
        options.max_seconds = args.max_seconds
    options.problem = resolve_problem(args, options)
    return options


def resolve_problem(args: argparse.Namespace, options: RunOptions) -> str:
    if args.file:
        return Path(args.file).read_text(encoding="utf-8").strip()
    if args.problem:
        return args.problem.strip()
    if options.problem:
        return options.problem
    if options.resume:
        # The resumed graph carries the problem, so there is nothing to ask for.
        return ""
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return input("Mathematical problem: ").strip()


def build_summary(supervisor: Supervisor) -> str:
    """Assemble the final report from the graph plus the planner's own summary."""
    graph = supervisor.graph
    lines = [
        "# Research summary",
        "",
        "## Problem",
        "",
        graph.problem.strip(),
        "",
        "## Outcome",
        "",
        f"Stopped because: {supervisor.finish_reason or 'unknown'}.",
        f"Graph: {graph.stats_line()}.",
        f"Planner calls: {supervisor.planner_calls}. Worker calls: {supervisor.worker_calls}. "
        f"Elapsed: {supervisor.elapsed:.0f}s.",
        f"Model usage: {USAGE.summary()}.",
        "",
    ]

    if supervisor.final_summary.strip():
        lines += ["## Director's report", "", supervisor.final_summary.strip(), ""]

    sections = [
        ("Promising directions", ("PROMISING",)),
        ("Obstacles", ("OBSTACLE",)),
        ("Open ideas and questions", ("IDEA", "UNVERIFIED")),
        ("Literature", ("POTENTIALLY_RELEVANT",)),
        ("Dead ends and rejected claims", ("DEAD_END", "REJECTED")),
    ]
    for title, statuses in sections:
        nodes = [n for n in graph.by_status(*statuses) if n["id"] != "problem"]
        if not nodes:
            continue
        nodes.sort(key=lambda n: n["created_at"])
        lines += [f"## {title}", ""]
        for node in nodes:
            content = " ".join(node["content"].split())
            lines.append(f"- **[{node['id']}]** ({node['type']}, by {node['created_by']}) {content}")
        lines.append("")

    if graph.edges:
        lines += ["## Connections", ""]
        for edge in graph.edges:
            lines.append(f"- {edge['source']} --{edge['relation']}--> {edge['target']}")
        lines.append("")

    lines += [
        "---",
        "",
        "Nothing above is verified. Statuses record how the system judged each "
        "claim, not whether it is true.",
    ]
    return "\n".join(lines)


async def run(options: RunOptions) -> int:
    try:
        config.require_api_keys()
    except config.MissingAPIKey as exc:
        print(exc, file=sys.stderr)
        return 1

    problem = options.problem
    if not problem and not options.resume:
        print("No problem given. Set [run] problem in run_config.toml.", file=sys.stderr)
        return 1

    run_dir = new_run_dir(config.RUNS_DIR, options.tag)
    log = RunLog(run_dir)
    set_note_sink(log.line)

    if options.resume:
        graph = load_graph(Path(options.resume) / "graph.json")
        problem = problem or graph.problem
        if not problem:
            print(f"{options.resume} has no stored problem; set one.", file=sys.stderr)
            log.close()
            return 1
        graph.data["problem"] = problem
        log.line("System", f"resumed graph from {options.resume} ({graph.stats_line()})")
    else:
        graph = ResearchGraph(problem)
    attach_autosave(graph, log.graph_path)

    options.problem = problem
    viewer = None
    if config.VIEWER_ENABLED:
        try:
            viewer = start_viewer(
                run_dir,
                port=config.VIEWER_PORT,
                open_browser=config.VIEWER_OPEN_BROWSER,
                poll_ms=config.VIEWER_POLL_MS,
            )
        except Exception as exc:  # noqa: BLE001 - a viewer must never stop a run
            log.error(f"viewer could not start: {type(exc).__name__}: {exc}")

    log.rule("Agentic mathematical research")
    log.line("System", f"run directory: {run_dir}")
    if viewer is not None:
        log.line("System", f"live graph: {viewer.url}")
    log.write_config(config.render_redacted_toml(config.RUN_CONFIG, options))
    for warning in config.RUN_CONFIG.warnings:
        log.line("System", f"config warning: {warning}")
    for line in config.banner_lines(MAIN_ROLES):
        log.line("System", line)
    log.line(
        "System",
        "worker slots: flex_1..flex_6, any role per assignment "
        "(searcher, toy_example, counterexample, decomposer, sketcher, verifier); "
        "all slots share the [api_keys].keys pool",
    )
    log.line("System", f"problem: {problem}")

    supervisor = Supervisor(
        problem=problem,
        graph=graph,
        planner=Planner(problem),
        log=log,
        max_planner_calls=options.max_planner_calls,
        max_worker_calls=options.max_worker_calls,
        max_seconds=options.max_seconds,
    )

    seed = Event(type="user_message", source="user", payload={"text": problem})
    try:
        await supervisor.run(seed)
    except (KeyboardInterrupt, asyncio.CancelledError):
        supervisor.finish_reason = "interrupted by user"
        log.line("System", "interrupted; shutting down")
        await supervisor.shutdown()
    finally:
        summary = build_summary(supervisor)
        log.write_summary(summary)
        log.rule("Done")
        log.line("System", f"stopped: {supervisor.finish_reason or 'unknown'}")
        log.line("System", f"graph: {graph.stats_line()}")
        log.line("System", USAGE.summary())
        log.line("System", f"summary written to {log.summary_path}")
        try:
            from .report import recreate_and_compile
            graph_html, compiled_md = recreate_and_compile(run_dir, open_browser=False)
            log.line("System", f"interactive graph: {graph_html}")
            log.line("System", f"compiled results: {compiled_md}")
        except Exception as exc:  # noqa: BLE001
            log.line("System", f"report compilation skipped: {exc}")
        if viewer is not None:
            log.line(
                "System",
                "reopen the graph later with: python -m math_agent.viewer "
                f"--run {run_dir}",
            )
            viewer.stop()
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
