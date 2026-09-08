"""A live, read-only window onto a run's research graph.

The run already writes `graph.json` after every graph mutation and appends to
`events.jsonl` as each event lands, so this needs no hook into the event loop:
it watches those two files and serves them to a browser. Nothing here can
mutate the graph or influence a run, and the server is bound to the loopback
interface only.

    from .viewer import start_viewer
    viewer = start_viewer(run_dir)
    ...
    viewer.stop()
"""

from __future__ import annotations

import json
import threading
import time
import webbrowser
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

PAGE_PATH = Path(__file__).resolve().parent / "page.html"

HOST = "127.0.0.1"

# Event feed entries are one-liners; worker results can be thousands of
# characters and the browser has no use for the whole thing.
MAX_HEADLINE_CHARS = 220

# How long to keep in the feed. Older entries are dropped from memory, but the
# client keeps whatever it has already been sent.
MAX_EVENTS_HELD = 2000


@dataclass
class Viewer:
    """A running viewer server."""

    url: str
    port: int
    run_dir: Path
    _server: ThreadingHTTPServer
    _thread: threading.Thread

    def stop(self) -> None:
        """Shut the server down; safe to call more than once."""
        try:
            self._server.shutdown()
            self._server.server_close()
        except Exception:  # noqa: BLE001 - shutting down must never raise
            pass
        self._thread.join(timeout=2.0)


class RunWatcher:
    """Tracks one run directory, re-reading only what has changed."""

    def __init__(self, run_dir: str | Path, poll_ms: int = 1000) -> None:
        self.run_dir = Path(run_dir)
        self.poll_ms = poll_ms
        self.graph_path = self.run_dir / "graph.json"
        self.events_path = self.run_dir / "events.jsonl"
        self.summary_path = self.run_dir / "summary.md"

        self._lock = threading.Lock()
        self._graph: dict[str, Any] = {"problem": "", "nodes": {}, "edges": []}
        self._graph_stamp: tuple[float, int] | None = None
        self._events: list[dict[str, Any]] = []
        self._events_seen = 0
        self._offset = 0
        self._partial = b""

    # -- reading ------------------------------------------------------------

    def _refresh_graph(self) -> bool:
        """Re-read graph.json if it has changed. True when it did."""
        try:
            stat = self.graph_path.stat()
        except OSError:
            return False
        stamp = (stat.st_mtime, stat.st_size)
        if stamp == self._graph_stamp:
            return False

        # save_graph writes a temp file and os.replace()s it, so a reader sees
        # either the old file or the new one. On Windows the replace itself can
        # still briefly refuse a concurrent open, hence the retry.
        for attempt in range(3):
            try:
                data = json.loads(self.graph_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                time.sleep(0.05 * (attempt + 1))
                continue
            if isinstance(data, dict):
                self._graph = {
                    "problem": data.get("problem", ""),
                    "nodes": data.get("nodes", {}) or {},
                    "edges": data.get("edges", []) or [],
                }
                self._graph_stamp = stamp
                return True
        # Keep serving the last good snapshot rather than failing the request.
        return False

    def _refresh_events(self) -> None:
        """Read whatever has been appended to events.jsonl since last time."""
        try:
            size = self.events_path.stat().st_size
        except OSError:
            return
        if size < self._offset:  # a different run, or a truncated file
            self._offset = 0
            self._partial = b""
            self._events.clear()
            self._events_seen = 0
        if size == self._offset:
            return

        try:
            with self.events_path.open("rb") as handle:
                handle.seek(self._offset)
                chunk = handle.read()
        except OSError:
            return
        self._offset += len(chunk)

        lines = (self._partial + chunk).split(b"\n")
        self._partial = lines.pop()  # the last line may still be being written
        for line in lines:
            if not line.strip():
                continue
            try:
                record = json.loads(line.decode("utf-8", "replace"))
            except json.JSONDecodeError:
                continue
            self._events.append(summarise_event(record, self._events_seen))
            self._events_seen += 1
        if len(self._events) > MAX_EVENTS_HELD:
            del self._events[: len(self._events) - MAX_EVENTS_HELD]

    # -- serving ------------------------------------------------------------

    def state(self, *, events_from: int = 0, full: bool = False) -> dict[str, Any]:
        """The whole current state, or a bare `changed: false` when idle."""
        with self._lock:
            graph_changed = self._refresh_graph()
            self._refresh_events()

            if not full and not graph_changed and events_from >= self._events_seen:
                return {"changed": False}

            held_from = self._events_seen - len(self._events)
            start = max(events_from, held_from) - held_from
            new_events = self._events[max(start, 0) :]

            nodes = self._graph["nodes"]
            counts: dict[str, int] = {}
            for node in nodes.values():
                status = str(node.get("status", "IDEA"))
                counts[status] = counts.get(status, 0) + 1

            return {
                "changed": True,
                "run": self.run_dir.name,
                "run_dir": str(self.run_dir),
                "problem": self._graph["problem"],
                "nodes": nodes,
                "edges": self._graph["edges"],
                "stats": {
                    "nodes": len(nodes),
                    "edges": len(self._graph["edges"]),
                    "by_status": counts,
                },
                "events": new_events,
                "events_total": self._events_seen,
                "finished": self.summary_path.exists(),
                "poll_ms": self.poll_ms,
            }


def _clip(text: Any, limit: int = MAX_HEADLINE_CHARS) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


def summarise_event(record: dict[str, Any], index: int) -> dict[str, Any]:
    """Reduce one events.jsonl record to a feed line."""
    kind = str(record.get("event", "event"))
    source = str(record.get("source", "system"))
    payload = record.get("payload") or {}
    if not isinstance(payload, dict):
        payload = {}

    if kind == "graph_action":
        action = record.get("action") or {}
        action_type = str(action.get("type", "?")) if isinstance(action, dict) else "?"
        headline = f"{action_type}: {_clip(record.get('result', ''))}"
        source = "planner"
    elif kind == "worker_result":
        headline = f"finished: {_clip(payload.get('task', ''))}"
    elif kind == "task_failed":
        headline = f"failed: {_clip(payload.get('error', ''))}"
    elif kind == "search_result":
        headline = (
            f"{payload.get('count', 0)} results for {_clip(payload.get('query', ''), 90)}"
        )
    elif kind == "paper_retrieved":
        headline = f"retrieved {_clip(payload.get('title', ''), 120)}"
    elif kind == "user_message":
        headline = "problem stated"
    elif kind == "system_idle":
        headline = "nothing in flight"
    else:
        headline = _clip(payload.get("task") or payload.get("text") or "")

    return {
        "i": index,
        "ts": record.get("ts", 0.0),
        "event": kind,
        "source": source,
        "headline": headline,
    }


class _Handler(BaseHTTPRequestHandler):
    server_version = "math-agent-viewer"

    @property
    def watcher(self) -> RunWatcher:
        return self.server.watcher  # type: ignore[attr-defined]

    def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler's naming
        try:
            route = urlparse(self.path)
            if route.path in ("/", "/index.html"):
                self._send_page()
            elif route.path == "/api/state":
                self._send_state(parse_qs(route.query))
            else:
                self._send_json({"error": "not found"}, status=404)
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError):
            pass  # the browser navigated away mid-response
        except Exception as exc:  # noqa: BLE001 - a viewer bug must not look like a crash
            try:
                self._send_json({"error": f"{type(exc).__name__}: {exc}"}, status=500)
            except Exception:  # noqa: BLE001
                pass

    def _send_page(self) -> None:
        body = PAGE_PATH.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_state(self, query: dict[str, list[str]]) -> None:
        try:
            events_from = int(query.get("events_from", ["0"])[0])
        except ValueError:
            events_from = 0
        full = query.get("full", ["0"])[0] not in ("0", "", "false")
        self._send_json(self.watcher.state(events_from=events_from, full=full))

    def _send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args: Any) -> None:
        """Silence the default access log; the run's console owns stderr."""


class _Server(ThreadingHTTPServer):
    daemon_threads = True  # never hold up interpreter exit

    # HTTPServer sets SO_REUSEADDR, which on Windows lets a second server bind a
    # port another one is already listening on: two viewers would then split the
    # requests. Refusing that is what makes the port fallback below work.
    allow_reuse_address = False

    def __init__(self, address: tuple[str, int], watcher: RunWatcher) -> None:
        super().__init__(address, _Handler)
        self.watcher = watcher


def start_viewer(
    run_dir: str | Path,
    *,
    port: int = 8765,
    open_browser: bool = True,
    poll_ms: int = 1000,
) -> Viewer:
    """Serve a live view of `run_dir` on localhost and return the handle.

    Falls back to an OS-assigned port if the requested one is taken, so a second
    run never fails just because the first one is still on screen.
    """
    watcher = RunWatcher(run_dir, poll_ms=poll_ms)
    try:
        server = _Server((HOST, port), watcher)
    except OSError:
        server = _Server((HOST, 0), watcher)

    actual_port = server.server_address[1]
    url = f"http://{HOST}:{actual_port}/"

    thread = threading.Thread(target=server.serve_forever, name="viewer", daemon=True)
    thread.start()

    if open_browser:
        # In a thread: opening a browser can block for a noticeable moment.
        threading.Thread(
            target=lambda: webbrowser.open(url), name="viewer-open", daemon=True
        ).start()

    return Viewer(url=url, port=actual_port, run_dir=Path(run_dir), _server=server, _thread=thread)


def export_standalone_html(
    run_dir: str | Path,
    output_path: str | Path | None = None,
) -> Path:
    """Generate a self-contained interactive HTML file of the run's graph.

    Embeds all nodes, edges, statistics, and event log into the page so it can
    be opened locally or shared without running a web server.
    """
    run_path = Path(run_dir)
    watcher = RunWatcher(run_path)
    state = watcher.state(full=True)

    html_template = PAGE_PATH.read_text(encoding="utf-8")
    state_json = (
        json.dumps(state, ensure_ascii=False)
        .replace("</script>", "<\\/script>")
        .replace("<!--", "<\\!--")
    )
    injection = f"<script>\nwindow.STATIC_STATE = {state_json};\n</script>\n<script>"

    if "<script>" in html_template:
        bundled_html = html_template.replace("<script>", injection, 1)
    else:
        bundled_html = f"<script>window.STATIC_STATE = {state_json};</script>\n" + html_template

    target = Path(output_path) if output_path else run_path / "interactive_graph.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(bundled_html, encoding="utf-8")
    return target


def newest_run_dir(runs_dir: str | Path) -> Path | None:
    """The most recently touched run directory that has a graph to show."""
    runs_dir = Path(runs_dir)
    if not runs_dir.is_dir():
        return None
    candidates = [d for d in runs_dir.iterdir() if d.is_dir() and (d / "graph.json").exists()]
    if not candidates:
        return None
    return max(candidates, key=lambda d: (d / "graph.json").stat().st_mtime)
