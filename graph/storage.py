"""JSON persistence for the research graph."""

from __future__ import annotations

import json
import os
from pathlib import Path

from .graph import ResearchGraph


def save_graph(graph: ResearchGraph, path: str | Path) -> None:
    """Write the graph to JSON, replacing the previous file atomically."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        json.dump(graph.to_dict(), handle, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


def load_graph(path: str | Path) -> ResearchGraph:
    """Load a graph written by save_graph."""
    with Path(path).open(encoding="utf-8") as handle:
        return ResearchGraph.from_dict(json.load(handle))


def attach_autosave(graph: ResearchGraph, path: str | Path) -> None:
    """Persist the graph after every mutation."""
    graph.set_change_hook(lambda g: save_graph(g, path))
    save_graph(graph, path)
