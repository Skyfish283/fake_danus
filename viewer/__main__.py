"""Watch a run's research graph in a browser, from its own window.

    python -m math_agent.viewer
    python -m math_agent.viewer --run math_agent/runs/20260821-221418
    python -m math_agent.viewer --port 9000 --no-open

With no arguments it picks the most recently written run under `runs/`, which is
the run in progress if one is going. It only reads files, so it is equally happy
watching a live run or replaying a finished one.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

if __package__ in ("", "viewer", None):
    _top = Path(__file__).resolve().parent.parent
    if str(_top.parent) not in sys.path:
        sys.path.insert(0, str(_top.parent))
    if str(_top) not in sys.path:
        sys.path.insert(0, str(_top))
    try:
        from math_agent import config
        from math_agent.viewer import export_standalone_html, newest_run_dir, start_viewer
    except ImportError:
        import config  # type: ignore
        from viewer import export_standalone_html, newest_run_dir, start_viewer  # type: ignore
else:
    from .. import config
    from . import export_standalone_html, newest_run_dir, start_viewer


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m math_agent.viewer",
        description="Serve a live view of a run's research graph on localhost or export static HTML.",
    )
    parser.add_argument(
        "--run", help="Run directory to watch (default: the newest one under runs/)."
    )
    parser.add_argument(
        "--port", type=int, default=config.VIEWER_PORT,
        help=f"Port to serve on, 0 for any free port (config: {config.VIEWER_PORT}).",
    )
    parser.add_argument(
        "--no-open", action="store_true", help="Do not open a browser window."
    )
    parser.add_argument(
        "--poll-ms", type=int, default=config.VIEWER_POLL_MS,
        help=f"How often the page asks for changes (config: {config.VIEWER_POLL_MS}).",
    )
    parser.add_argument(
        "--export", action="store_true",
        help="Export a standalone interactive HTML graph file that works offline.",
    )
    parser.add_argument(
        "--output",
        help="Output path for --export (default: <run_dir>/interactive_graph.html).",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if args.run:
        run_dir = Path(args.run)
        if not run_dir.is_dir():
            print(f"{run_dir} is not a directory.", file=sys.stderr)
            return 1
    else:
        found = newest_run_dir(config.RUNS_DIR)
        if found is None:
            print(
                f"No run with a graph.json found under {config.RUNS_DIR}.\n"
                "Start a run first, or pass --run <directory>.",
                file=sys.stderr,
            )
            return 1
        run_dir = found

    if args.export:
        import webbrowser
        out = export_standalone_html(run_dir, args.output)
        print(f"Exported interactive graph to {out}")
        if not args.no_open:
            webbrowser.open(out.resolve().as_uri())
        return 0

    viewer = start_viewer(
        run_dir,
        port=args.port,
        open_browser=not args.no_open,
        poll_ms=args.poll_ms,
    )
    print(f"Watching {run_dir}")
    print(f"Viewer at {viewer.url}  (Ctrl-C to stop)")

    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        print("\nStopping.")
    finally:
        viewer.stop()
    return 0


if __name__ == "__main__":
    sys.exit(main())
