"""Timestamped logging to the console, a transcript file, and events.jsonl."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Any

from rich.console import Console


def _ensure_utf8_stdout() -> None:
    """Model output contains mathematical symbols; a cp1252 console would raise."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001 - not all streams are reconfigurable
            pass

_STYLES = {
    "Gemini": "bold cyan",
    "System": "dim",
    "searcher": "green",
    "toy_example": "green",
    "sketcher": "yellow",
    "decomposer": "yellow",
    "counterexample": "magenta",
    "verifier": "magenta",
    "Papers": "blue",
    "Error": "bold red",
}


class RunLog:
    """One run's console output and on-disk record."""

    def __init__(self, run_dir: str | Path) -> None:
        self.run_dir = Path(run_dir)
        self.run_dir.mkdir(parents=True, exist_ok=True)
        self.graph_path = self.run_dir / "graph.json"
        self.events_path = self.run_dir / "events.jsonl"
        self.transcript_path = self.run_dir / "log.txt"
        self.summary_path = self.run_dir / "summary.md"
        self.config_path = self.run_dir / "config_used.toml"

        _ensure_utf8_stdout()
        self.console = Console()
        self._transcript = self.transcript_path.open("a", encoding="utf-8")
        self._events = self.events_path.open("a", encoding="utf-8")

    # -- console ------------------------------------------------------------

    def line(self, actor: str, message: str, *, detail: str = "") -> None:
        stamp = time.strftime("%H:%M:%S")
        style = _STYLES.get(actor, "white")
        self._print(f"[dim]\\[{stamp}][/dim] [{style}]{actor}[/{style}] {_escape(message)}")
        text = f"[{stamp}] {actor} {message}"
        if detail:
            self._print(f"           [dim]{_escape(detail)}[/dim]")
            text += f"\n           {detail}"
        self._transcript.write(text + "\n")
        self._transcript.flush()

    def rule(self, title: str) -> None:
        self.console.rule(f"[bold]{title}")
        self._transcript.write(f"\n===== {title} =====\n")
        self._transcript.flush()

    def _print(self, markup: str) -> None:
        try:
            self.console.print(markup)
        except UnicodeEncodeError:
            self.console.print(markup.encode("ascii", "replace").decode("ascii"))

    def block(self, title: str, body: str) -> None:
        """Write a long block to the transcript, and a short form to console."""
        self._print(f"[dim]{_escape(_clip(body, 400))}[/dim]")
        self._transcript.write(f"--- {title} ---\n{body}\n--- end {title} ---\n")
        self._transcript.flush()

    def error(self, message: str) -> None:
        self.line("Error", message)

    # -- structured record --------------------------------------------------

    def record_event(self, payload: dict[str, Any]) -> None:
        self._events.write(json.dumps({"ts": time.time(), **payload}, ensure_ascii=False) + "\n")
        self._events.flush()

    def write_summary(self, text: str) -> None:
        self.summary_path.write_text(text, encoding="utf-8")

    def write_config(self, text: str) -> None:
        """Record the settings this run used, so the result is reproducible."""
        self.config_path.write_text(text, encoding="utf-8")

    def close(self) -> None:
        for handle in (self._transcript, self._events):
            try:
                handle.close()
            except Exception:  # noqa: BLE001 - closing must not break shutdown
                pass


def _clip(text: str, limit: int) -> str:
    text = text.strip()
    return text if len(text) <= limit else text[:limit] + " [...]"


def _escape(text: str) -> str:
    """Stop stray square brackets in model output being read as rich markup."""
    return str(text).replace("[", "\\[")


def new_run_dir(base: str | Path, tag: str = "") -> Path:
    stamp = time.strftime("%Y%m%d-%H%M%S")
    name = f"{stamp}-{tag}" if tag else stamp
    path = Path(base) / name
    path.mkdir(parents=True, exist_ok=True)
    return path
