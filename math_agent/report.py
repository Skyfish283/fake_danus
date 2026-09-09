"""Recreate interactive graphs and compile research results from math_agent runs.

This module provides:
1. Recreating the interactive research graph for any run in `runs/`:
   - Standalone, self-contained HTML export (`interactive_graph.html`) that works
     offline in any browser without Python or a server running.
   - Interactive live viewer HTTP server on localhost.
2. Compiling all results from a run into a single Markdown document:
   - Full metadata, configuration, Director's report, research graph catalog,
     unabridged worker derivations/proofs, literature search results, and timeline.
   - Preceded by a structured, publication-grade prompt instructing an LLM to
     synthesize the raw experimental findings into a formal research report.

Usage:
    python -m math_agent.report --all                              # newest run
    python -m math_agent.report --run runs/20260821-222552 --all
    python -m math_agent.report --run runs/20260821-222552 --graph
    python -m math_agent.report --run runs/20260821-222552 --compile
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import webbrowser
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Ensure both package imports and standalone script execution work seamlessly
_pkg_root = Path(__file__).resolve().parent
_parent_root = _pkg_root.parent
for _p in (str(_parent_root), str(_pkg_root)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

try:
    from math_agent import config
    from math_agent.graph.graph import ResearchGraph
    from math_agent.viewer import Viewer, export_standalone_html, newest_run_dir, start_viewer
except ImportError:
    import config  # type: ignore
    from graph.graph import ResearchGraph  # type: ignore
    from viewer import Viewer, export_standalone_html, newest_run_dir, start_viewer  # type: ignore


# ============================================================================
# 1. Graph Reconstruction and Interactive Graph Recreation
# ============================================================================

def reconstruct_graph_from_events(events_path: str | Path) -> ResearchGraph:
    """Rebuild a ResearchGraph by replaying graph_action events from events.jsonl.

    Useful as a fallback if graph.json is missing or corrupted.
    """
    events_file = Path(events_path)
    if not events_file.is_file():
        raise FileNotFoundError(f"Events file not found: {events_file}")

    graph = ResearchGraph()
    problem_text = ""

    with events_file.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue

            event_type = rec.get("event")
            payload = rec.get("payload") or {}

            if event_type == "user_message" and not problem_text:
                problem_text = str(payload.get("text", ""))
                if problem_text and "problem" not in graph.nodes:
                    graph.data["problem"] = problem_text
                    graph.add_node(
                        node_type="problem",
                        content=problem_text,
                        status="UNVERIFIED",
                        created_by="user",
                        node_id="problem",
                    )

            elif event_type == "graph_action":
                action = rec.get("action") or {}
                act_type = action.get("type", "")
                if act_type == "ADD_NODE":
                    c = action.get("content") or action.get("summary") or ""
                    if c:
                        graph.add_node(
                            node_type=action.get("node_type", "note"),
                            content=c,
                            status=action.get("status", "IDEA"),
                            created_by=rec.get("source", "planner"),
                            node_id=action.get("node_id"),
                        )
                elif act_type == "UPDATE_NODE":
                    nid = action.get("node_id", "")
                    if nid and graph.exists(nid):
                        graph.update_node(
                            nid,
                            status=action.get("status"),
                            content=action.get("content"),
                            note=action.get("note"),
                            updated_by=rec.get("source", "planner"),
                        )
                elif act_type == "ADD_EDGE":
                    s = action.get("source", "")
                    t = action.get("target", "")
                    rel = action.get("relation", "related_to")
                    if s and t:
                        graph.add_edge(s, t, rel)

    return graph


def export_interactive_graph(
    run_dir: str | Path,
    output_file: str | Path | None = None,
    open_browser: bool = False,
) -> Path:
    """Generate a self-contained offline interactive HTML graph from a run directory."""
    run_path = Path(run_dir)
    if not run_path.is_dir():
        raise NotADirectoryError(f"Run directory not found: {run_path}")

    # Ensure graph.json exists, reconstruct if needed
    graph_json_path = run_path / "graph.json"
    if not graph_json_path.exists():
        events_jsonl_path = run_path / "events.jsonl"
        if events_jsonl_path.exists():
            reconstructed = reconstruct_graph_from_events(events_jsonl_path)
            graph_json_path.write_text(
                json.dumps(reconstructed.to_dict(), indent=2, ensure_ascii=False),
                encoding="utf-8",
            )

    out_path = export_standalone_html(run_path, output_file)
    if open_browser:
        webbrowser.open(out_path.resolve().as_uri())
    return out_path


def view_run_graph(
    run_dir: str | Path,
    port: int = 8765,
    open_browser: bool = True,
    poll_ms: int = 1000,
) -> Viewer:
    """Launch the live HTTP viewer server for a run."""
    run_path = Path(run_dir)
    if not run_path.is_dir():
        raise NotADirectoryError(f"Run directory not found: {run_path}")
    return start_viewer(run_path, port=port, open_browser=open_browser, poll_ms=poll_ms)


def recreate_interactive_graph(
    run_dir: str | Path,
    output_file: str | Path | None = None,
    open_browser: bool = True,
    serve: bool = False,
    port: int = 8765,
) -> Path | Viewer:
    """Recreate the interactive graph for a run.

    If `serve` is True, starts a local HTTP viewer server.
    Otherwise, generates a self-contained offline HTML file and opens it in the browser.
    """
    if serve:
        return view_run_graph(run_dir, port=port, open_browser=open_browser)
    return export_interactive_graph(run_dir, output_file=output_file, open_browser=open_browser)


# ============================================================================
# 2. Results Compilation & LLM Report Prompt Generation
# ============================================================================

LLM_REPORT_INSTRUCTIONS = """# Instructions for LLM: Authoring the Mathematical Research Report

> [!IMPORTANT]
> **ROLE AND OBJECTIVE**
> You are an elite Research Mathematician and Theoretical Computer Scientist acting as Principal Investigator.
> Below are the comprehensive raw artifacts from an automated agentic mathematical research run, including:
> - Problem definition and runtime parameters
> - High-level Director's synthesis
> - The complete research graph (hypotheses, proved lemmas, identified obstacles, literature connections)
> - Unabridged worker derivations from the Mathematician, Explorer, and Skeptic roles
> - Literature retrieval and search results
>
> Your task is to analyze this dossier and write an exhaustive, publication-grade, mathematically rigorous **Research Report**.

## Required Report Sections

1. **Title & Executive Summary**
   - Provide a formal, descriptive title for the research paper/report.
   - Formulate a clear Abstract and Executive Summary synthesizing the core findings.
   - Summarize what was definitively proven, what promising conjectures were substantiated, and what fundamental barriers remain.

2. **Problem Formalization & Scope**
   - Rigorously define the sequence, series, dynamical system, or model under investigation.
   - Detail any structural reductions or reformulation lemmas discovered during the run (e.g., recurrence reduction from non-local sums to single-step recurrences, continuous embedding, etc.).
   - Explicitly define the parameter regimes explored (e.g. boundary values, small vs. large regimes, negative values, complex numbers, $p$-adic fields $\\mathbb{Q}_p$).

3. **Rigorous Analysis of Lemmas & Promising Directions**
   - Present every major lemma, theorem, or promising approach established in the run.
   - For every claim, cite its corresponding node ID from the research graph (e.g., `[lemma_1]`, `[lemma_2]`, `[approach_10]`).
   - Carefully reconstruct, polish, and verify the mathematical proofs. Critically evaluate whether any proofs contain hidden assumptions, heuristic gaps, or unverified claims.

4. **Obstacles, Structural Barriers & Counterexamples**
   - Thoroughly analyze each obstacle identified by the research system (cite nodes like `[obstacle_1]`, `[obstacle_2]`).
   - Explain why standard methods fail (e.g., parity/sign oscillation destroying monotonicity, non-autonomous exponents preventing fixed-point theorems, superexponential growth, infinite moment hierarchies).
   - Distinguish fundamental mathematical impossibility/divergence results from technical obstacles that could potentially be bypassed with more refined techniques.

5. **Worker Perspective Comparison & Dialectic Synthesis**
   - Compare and contrast the different angles provided by the specialized agents:
     * **Mathematician**: Analytical bounds, asymptotic rates, classical convergence tests, algebraic manipulations.
     * **Explorer**: Unconventional reframings (continuous analogues, dynamical systems, $p$-adic valuations, root-landing absorbing states).
     * **Skeptic**: Boundary attacks, superexponential blow-up proofs, counterexamples, instability criteria.
   - Critique where the roles complemented or challenged each other, and summarize the consensus.

6. **Literature & Theoretical Context**
   - Integrate any papers or literature searches retrieved during the run.
   - Contextualize the findings within relevant mathematical literature (e.g., non-autonomous difference equations, ultrametric analysis, branching processes, etc.).

7. **Concrete Actionable Research Roadmap**
   - Provide a prioritized, numbered list of concrete next steps for human mathematicians or future agent runs.
   - Detail specific conjectures to formalize, boundary constants to compute, or numerical experiments to perform.

8. **Traceability Index**
   - Provide a concise reference table mapping key findings to their graph node IDs and worker task IDs.

## Mathematical Formatting & Tone Requirements
- Use formal academic mathematical prose with precise terminology.
- Render all formulas in clean LaTeX (`$ ... $` for inline formulas, `$$ ... $$` for display equations).
- Be intellectually honest: clearly separate verified rigorous proofs from heuristic intuitions or unproven conjectures.
"""


def _load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _format_timestamp(ts: float | int | None) -> str:
    if not ts:
        return "N/A"
    try:
        return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    except Exception:
        return str(ts)


def compile_run_to_markdown(
    run_dir: str | Path,
    output_file: str | Path | None = None,
    custom_instructions: str | None = None,
) -> Path:
    """Compile all results from a run into a single comprehensive Markdown dossier."""
    run_path = Path(run_dir)
    if not run_path.is_dir():
        raise NotADirectoryError(f"Run directory not found: {run_path}")

    # Artifact paths
    graph_path = run_path / "graph.json"
    events_path = run_path / "events.jsonl"
    summary_path = run_path / "summary.md"
    config_path = run_path / "config_used.toml"
    log_path = run_path / "log.txt"

    # 1. Load Graph
    graph_data = _load_json(graph_path)
    if not graph_data and events_path.is_file():
        reconstructed = reconstruct_graph_from_events(events_path)
        graph_data = reconstructed.to_dict()

    problem_text = graph_data.get("problem", "")
    nodes: dict[str, dict[str, Any]] = graph_data.get("nodes", {})
    edges: list[dict[str, Any]] = graph_data.get("edges", [])

    # 2. Load Events
    events: list[dict[str, Any]] = []
    worker_results: list[dict[str, Any]] = []
    literature_events: list[dict[str, Any]] = []
    graph_actions: list[dict[str, Any]] = []
    first_ts: float | None = None
    last_ts: float | None = None

    if events_path.is_file():
        with events_path.open("r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                events.append(rec)

                ts = rec.get("ts")
                if ts:
                    if first_ts is None or ts < first_ts:
                        first_ts = ts
                    if last_ts is None or ts > last_ts:
                        last_ts = ts

                ev_type = rec.get("event")
                if ev_type == "user_message" and not problem_text:
                    payload = rec.get("payload") or {}
                    problem_text = payload.get("text", "")
                elif ev_type == "worker_result":
                    worker_results.append(rec)
                elif ev_type in ("search_result", "paper_retrieved"):
                    literature_events.append(rec)
                elif ev_type == "graph_action":
                    graph_actions.append(rec)

    # 3. Load Summary
    summary_text = summary_path.read_text(encoding="utf-8") if summary_path.is_file() else ""

    # 4. Load Config
    config_text = config_path.read_text(encoding="utf-8") if config_path.is_file() else ""

    # 5. Compute stats
    status_counts: dict[str, int] = {}
    for node in nodes.values():
        st = node.get("status", "IDEA")
        status_counts[st] = status_counts.get(st, 0) + 1

    elapsed_str = "N/A"
    if first_ts and last_ts:
        dur = last_ts - first_ts
        mins, secs = divmod(int(dur), 60)
        elapsed_str = f"{mins}m {secs}s ({dur:.1f}s)"

    # Build output document
    lines: list[str] = []

    # Section 1: LLM Instructions
    instructions = custom_instructions if custom_instructions is not None else LLM_REPORT_INSTRUCTIONS
    lines.append(instructions.strip())
    lines.append("\n---\n")

    # Section 2: Run Overview & Metadata
    lines.append(f"# Dossier: Exploration Findings for `{run_path.name}`\n")
    lines.append("## Run Metadata\n")
    lines.append(f"- **Run Identifier**: `{run_path.name}`")
    lines.append(f"- **Run Directory**: `{run_path.resolve()}`")
    lines.append(f"- **Compiled At**: `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}`")
    lines.append(f"- **First Event Timestamp**: `{_format_timestamp(first_ts)}`")
    lines.append(f"- **Last Event Timestamp**: `{_format_timestamp(last_ts)}`")
    lines.append(f"- **Total Elapsed Time**: {elapsed_str}")
    lines.append(f"- **Total Graph Nodes**: {len(nodes)}")
    lines.append(f"- **Total Graph Edges**: {len(edges)}")
    lines.append(f"- **Worker Results Recorded**: {len(worker_results)}")
    lines.append(f"- **Total Events Logged**: {len(events)}")
    if status_counts:
        status_line = ", ".join(f"`{k}`: {v}" for k, v in sorted(status_counts.items()))
        lines.append(f"- **Node Breakdown by Status**: {status_line}")
    lines.append(f"- **Interactive Visual Graph**: Available as `interactive_graph.html` in this directory.")
    lines.append("")

    # Problem Formulation
    lines.append("## Problem Statement\n")
    lines.append("```text")
    lines.append(problem_text.strip() or "(No explicit problem recorded)")
    lines.append("```\n")

    # Section 3: Configuration Used
    if config_text.strip():
        lines.append("## Configuration Used\n")
        lines.append("```toml")
        lines.append(config_text.strip())
        lines.append("```\n")

    # Section 4: Director's Executive Report
    lines.append("# Director's Synthesis & System Summary\n")
    if summary_text.strip():
        lines.append(summary_text.strip())
    else:
        lines.append("*(No separate `summary.md` was written for this run.)*")
    lines.append("\n\n---\n")

    # Section 5: Complete Research Graph Catalog
    lines.append("# Research Graph State & Knowledge Catalog\n")
    lines.append(f"The graph contains **{len(nodes)} nodes** and **{len(edges)} directed edges**.\n")

    # Group nodes by status
    status_priority = [
        "PROMISING",
        "OBSTACLE",
        "IDEA",
        "UNVERIFIED",
        "POTENTIALLY_RELEVANT",
        "DEAD_END",
        "REJECTED",
    ]
    grouped_nodes: dict[str, list[dict[str, Any]]] = {}
    for node in nodes.values():
        st = node.get("status", "IDEA")
        grouped_nodes.setdefault(st, []).append(node)

    # Render each group
    for st in status_priority:
        group = grouped_nodes.get(st, [])
        if not group:
            continue
        lines.append(f"## Status: {st} ({len(group)} nodes)\n")
        for node in group:
            nid = node.get("id", "")
            ntype = node.get("type", "note")
            author = node.get("created_by", "unknown")
            content = node.get("content", "").strip()
            notes = node.get("notes", [])
            history = node.get("history", [])

            # Incoming/outgoing edges
            outgoing = [f"`{e.get('relation')}` -> `{e.get('target')}`" for e in edges if e.get("source") == nid]
            incoming = [f"`{e.get('source')}` -`{e.get('relation')}`-> this" for e in edges if e.get("target") == nid]

            lines.append(f"### `[{nid}]` ({ntype}, created by {author})\n")
            lines.append(f"**Content**:\n{content}\n")

            if notes:
                lines.append("**Attached Notes**:")
                for n in notes:
                    lines.append(f"- *{n.get('by', 'system')}*: {n.get('note', '')}")
                lines.append("")

            if history:
                lines.append("**Status History**:")
                for h in history:
                    lines.append(f"- {h.get('status_from')} -> {h.get('status_to')} (by {h.get('by', '')})")
                lines.append("")

            if outgoing or incoming:
                lines.append("**Graph Connections**:")
                if outgoing:
                    lines.append(f"- Outgoing: {'; '.join(outgoing)}")
                if incoming:
                    lines.append(f"- Incoming: {'; '.join(incoming)}")
                lines.append("")
        lines.append("")

    # Any other statuses
    remaining_statuses = [st for st in grouped_nodes if st not in status_priority]
    for st in remaining_statuses:
        group = grouped_nodes[st]
        lines.append(f"## Status: {st} ({len(group)} nodes)\n")
        for node in group:
            lines.append(f"### `[{node.get('id')}]` ({node.get('type')})\n{node.get('content', '')}\n")

    # Edges Table
    if edges:
        lines.append("## Graph Relations Index (Edges)\n")
        lines.append("| Source Node | Relation | Target Node |")
        lines.append("| :--- | :--- | :--- |")
        for edge in edges:
            lines.append(f"| `{edge.get('source')}` | `{edge.get('relation')}` | `{edge.get('target')}` |")
        lines.append("\n---\n")

    # Section 6: Full Worker Findings & Derivations
    lines.append("# Full Worker Findings & Derivations\n")
    lines.append(
        "Below are the complete, untruncated mathematical outputs produced by each specialist "
        "worker during the research exploration.\n"
    )

    if not worker_results:
        lines.append("*(No worker results were logged for this run.)*\n")
    else:
        for idx, wr in enumerate(worker_results, 1):
            source = wr.get("source", "worker")
            payload = wr.get("payload") or {}
            task_id = payload.get("task_id", f"task_{idx}")
            task = payload.get("task", "(No task description)")
            content = payload.get("content", "").strip()
            focus_nodes = payload.get("focus_nodes") or []
            elapsed = payload.get("elapsed")
            ts = wr.get("ts")

            header_meta = [f"Worker: **{source}**", f"Task ID: `{task_id}`"]
            if elapsed:
                header_meta.append(f"Duration: {elapsed:.1f}s")
            if ts:
                header_meta.append(f"Timestamp: {_format_timestamp(ts)}")
            if focus_nodes:
                header_meta.append(f"Focus Nodes: {', '.join(f'`{fn}`' for fn in focus_nodes)}")

            lines.append(f"## Finding #{idx}: {task_id} ({source.title()})\n")
            lines.append(f"*{' | '.join(header_meta)}*\n")
            lines.append(f"**Assigned Task Prompt**:\n> {task}\n")
            lines.append(f"**Worker Output & Derivations**:\n\n{content}\n")
            lines.append("---\n")

    # Section 7: Literature Search & Retrieved Works
    if literature_events:
        lines.append("# Literature & Paper Retrievals\n")
        for idx, ev in enumerate(literature_events, 1):
            payload = ev.get("payload") or {}
            ev_type = ev.get("event")
            if ev_type == "search_result":
                lines.append(f"### Search #{idx}: {payload.get('source', 'literature').title()}\n")
                lines.append(f"- **Query**: `{payload.get('query', '')}`")
                lines.append(f"- **Results Returned**: {payload.get('count', 0)}\n")
            elif ev_type == "paper_retrieved":
                lines.append(f"### Paper #{idx}: {payload.get('title', 'Unknown Title')}\n")
                lines.append(f"- **Authors**: {payload.get('authors', 'N/A')}")
                lines.append(f"- **Year**: {payload.get('year', 'N/A')}")
                lines.append(f"- **DOI/ID**: `{payload.get('paper_id', 'N/A')}`")
                if payload.get("summary"):
                    lines.append(f"- **Summary**: {payload.get('summary')}")
                lines.append("")
        lines.append("---\n")

    # Section 8: Graph Actions Chronology
    if graph_actions:
        lines.append("# Graph Evolution Chronology\n")
        lines.append("Chronological sequence of graph mutations decided by the planner:\n")
        lines.append("| Index | Time | Action Type | Details | Result |")
        lines.append("| :--- | :--- | :--- | :--- | :--- |")
        for idx, ga in enumerate(graph_actions, 1):
            ts_str = datetime.fromtimestamp(ga.get("ts", 0), tz=timezone.utc).strftime("%H:%M:%S") if ga.get("ts") else "-"
            act = ga.get("action") or {}
            act_type = act.get("type", "UNKNOWN")
            result = ga.get("result", "")
            target_info = act.get("node_id") or act.get("node_type") or f"{act.get('source')}->{act.get('target')}" or ""
            lines.append(f"| {idx} | {ts_str} | `{act_type}` | {target_info} | {result} |")
        lines.append("\n---\n")

    lines.append("*End of Compiled Research Dossier.*\n")

    full_markdown = "\n".join(lines)
    target_path = Path(output_file) if output_file else run_path / "compiled_results.md"
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(full_markdown, encoding="utf-8")
    return target_path


def recreate_and_compile(
    run_dir: str | Path,
    open_browser: bool = False,
) -> tuple[Path, Path]:
    """Execute both features on a run: export interactive graph and compile markdown dossier."""
    graph_html = export_interactive_graph(run_dir, open_browser=open_browser)
    compiled_md = compile_run_to_markdown(run_dir)
    return graph_html, compiled_md


# ============================================================================
# 3. CLI Entry Point
# ============================================================================

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m math_agent.report",
        description="Recreate interactive graphs and compile research results from math_agent runs.",
    )
    parser.add_argument(
        "--run",
        help="Path or name of the run directory (default: the newest one under runs/).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Recreate the interactive graph AND compile all results into markdown.",
    )
    parser.add_argument(
        "--graph",
        action="store_true",
        help="Recreate the interactive research graph.",
    )
    parser.add_argument(
        "--compile",
        action="store_true",
        help="Compile all results into one markdown file with LLM report instructions.",
    )
    parser.add_argument(
        "--output",
        help="Custom output file path for the compiled markdown or interactive graph.",
    )
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Serve the interactive graph with local HTTP server instead of generating static HTML.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=config.VIEWER_PORT,
        help=f"Port for HTTP viewer if --serve is used (default: {config.VIEWER_PORT}).",
    )
    parser.add_argument(
        "--no-open",
        action="store_true",
        help="Do not automatically open the browser.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    # Locate run directory
    if args.run:
        run_path = Path(args.run)
        if not run_path.is_dir():
            # Check if it was provided relative to config.RUNS_DIR
            alt_path = config.RUNS_DIR / args.run
            if alt_path.is_dir():
                run_path = alt_path
            else:
                print(f"Error: '{args.run}' is not a directory.", file=sys.stderr)
                return 1
    else:
        found = newest_run_dir(config.RUNS_DIR)
        if found is None:
            print(
                f"Error: No run directory with graph data found under {config.RUNS_DIR}.\n"
                "Please specify --run <directory>.",
                file=sys.stderr,
            )
            return 1
        run_path = found

    print(f"Processing run: {run_path}")

    # If neither --all, --graph, nor --compile was specified, default to --all
    do_all = args.all or (not args.graph and not args.compile)
    do_graph = do_all or args.graph
    do_compile = do_all or args.compile

    # Execute graph recreation
    if do_graph:
        if args.serve:
            print(f"Starting live viewer server for {run_path}...")
            viewer = view_run_graph(run_path, port=args.port, open_browser=not args.no_open)
            print(f"Viewer live at: {viewer.url} (Press Ctrl-C to stop)")
            try:
                while True:
                    time.sleep(1.0)
            except KeyboardInterrupt:
                print("\nStopping viewer.")
                viewer.stop()
        else:
            out_html = export_interactive_graph(
                run_path,
                output_file=args.output if (not do_compile and args.output) else None,
                open_browser=not args.no_open,
            )
            print(f"Interactive graph created: {out_html}")

    # Execute markdown compilation
    if do_compile:
        out_md = compile_run_to_markdown(
            run_path,
            output_file=args.output if (not do_graph and args.output) else None,
        )
        print(f"Results compiled to: {out_md}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
