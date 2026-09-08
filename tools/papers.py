"""Normalised paper records, search dispatch, and open-access full-text retrieval."""

from __future__ import annotations

import asyncio
import io
from dataclasses import dataclass, field
from typing import Any

import httpx

from .. import config

SOURCES = ("openalex", "semantic_scholar", "arxiv")


@dataclass
class Paper:
    """One paper, however it was found."""

    id: str
    title: str
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    abstract: str = ""
    doi: str = ""
    url: str = ""
    oa_url: str = ""
    venue: str = ""
    citations: int | None = None
    source: str = ""
    arxiv_id: str = ""

    def author_line(self, limit: int = 5) -> str:
        if not self.authors:
            return "unknown authors"
        shown = self.authors[:limit]
        suffix = " et al." if len(self.authors) > limit else ""
        return ", ".join(shown) + suffix

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "authors": self.authors,
            "year": self.year,
            "doi": self.doi,
            "url": self.url,
            "oa_url": self.oa_url,
            "venue": self.venue,
            "citations": self.citations,
            "source": self.source,
        }

    def render(self, index: int | None = None, abstract_chars: int = 1200) -> str:
        head = f"[{index}] " if index is not None else ""
        lines = [
            f"{head}Title: {self.title}",
            f"    Authors: {self.author_line()}",
            f"    Year: {self.year or 'unknown'}"
            + (f"   Venue: {self.venue}" if self.venue else "")
            + (f"   Citations: {self.citations}" if self.citations is not None else ""),
            f"    Paper id: {self.id}" + (f"   DOI: {self.doi}" if self.doi else ""),
            f"    Open access: {'yes' if self.oa_url else 'no'}",
        ]
        abstract = " ".join(self.abstract.split())
        if abstract:
            if len(abstract) > abstract_chars:
                abstract = abstract[:abstract_chars] + " [...truncated]"
            lines.append(f"    Abstract: {abstract}")
        else:
            lines.append("    Abstract: (not available)")
        return "\n".join(lines)


def render_results(papers: list[Paper], query: str, source: str) -> str:
    if not papers:
        return f"SEARCH RESULTS ({source}) for {query!r}\n\nNo results."
    body = "\n\n".join(paper.render(i + 1) for i, paper in enumerate(papers))
    return (
        f"SEARCH RESULTS ({source}) for {query!r}\n\n{body}\n\n"
        "Use GET_PAPER with one of the paper ids above to retrieve full text "
        "when an open-access version exists."
    )


# The backend modules import Paper from here, so they are imported lazily to
# keep the dependency one-directional.
def _backend(source: str):
    if source == "semantic_scholar":
        from . import semantic_scholar

        return semantic_scholar
    if source == "arxiv":
        from . import arxiv

        return arxiv
    from . import openalex

    return openalex


async def search_papers(query: str, source: str = "openalex", limit: int | None = None):
    """Search one backend, falling back to the others if it fails or is empty."""
    source = source if source in SOURCES else "openalex"
    order = [source] + [s for s in SOURCES if s != source]
    errors: list[str] = []

    for candidate in order:
        try:
            papers = await _backend(candidate).search(query, limit)
        except Exception as exc:  # noqa: BLE001 - try the next backend
            errors.append(f"{candidate}: {type(exc).__name__}: {exc}")
            continue
        if papers:
            return papers, candidate, errors
        errors.append(f"{candidate}: no results")
    return [], source, errors


async def _fetch_metadata(paper_id: str) -> Paper:
    prefix, _, _ = paper_id.partition(":")
    source = prefix if prefix in SOURCES else "openalex"
    if prefix not in SOURCES:
        # Bare ids: arXiv ids look like 2401.01234 or math/0211159.
        if paper_id.replace(".", "").replace("/", "").isdigit() or "/" in paper_id:
            source = "arxiv"
        elif paper_id.upper().startswith("W"):
            source = "openalex"
        else:
            source = "semantic_scholar"
    return await _backend(source).fetch(paper_id)


def _extract_pdf_text(data: bytes) -> str:
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    chunks: list[str] = []
    total = 0
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:  # noqa: BLE001 - a bad page should not lose the rest
            continue
        chunks.append(text)
        total += len(text)
        if total > config.MAX_PAPER_TEXT_CHARS:
            break
    return "\n".join(chunks)


async def _download_text(url: str) -> str:
    async with httpx.AsyncClient(
        timeout=config.HTTP_TIMEOUT_SECONDS,
        follow_redirects=True,
        headers={"User-Agent": f"math-agent-prototype ({config.OPENALEX_MAILTO})"},
    ) as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.content
        content_type = response.headers.get("content-type", "")

    if "pdf" in content_type.lower() or data[:4] == b"%PDF":
        return await asyncio.to_thread(_extract_pdf_text, data)
    return ""


async def get_paper(paper_id: str, known: Paper | None = None) -> tuple[Paper, str, str]:
    """Return (paper, text, note). `text` is full text when an OA PDF exists,
    otherwise the abstract; `note` explains which of the two it is.

    Pass `known` to reuse metadata already held from a search result.
    """
    paper = known or await _fetch_metadata(paper_id)

    if paper.oa_url:
        try:
            text = await _download_text(paper.oa_url)
        except Exception as exc:  # noqa: BLE001 - fall back to the abstract
            text = ""
            note = f"open-access download failed ({type(exc).__name__}); abstract only"
        else:
            note = ""
        if text.strip():
            if len(text) > config.MAX_PAPER_TEXT_CHARS:
                text = text[: config.MAX_PAPER_TEXT_CHARS] + "\n\n[...truncated]"
            return paper, text, "full text extracted from open-access PDF"
        if not note:
            note = "open-access link yielded no extractable text; abstract only"
    else:
        note = "no open-access version available; abstract only"

    if not paper.abstract.strip() and paper.doi:
        # OpenAlex often lacks abstracts for older work; Semantic Scholar
        # usually has one under the same DOI.
        try:
            from . import semantic_scholar

            fallback = await semantic_scholar.fetch(f"DOI:{paper.doi}")
        except Exception:  # noqa: BLE001 - the abstract simply stays missing
            pass
        else:
            if fallback.abstract.strip():
                paper.abstract = fallback.abstract
                note += "; abstract recovered from Semantic Scholar"

    return paper, paper.abstract, note


def render_paper(paper: Paper, text: str, note: str) -> str:
    header = paper.render()
    body = text.strip() or "(no text available)"
    return (
        f"PAPER RETRIEVED ({note})\n\n{header}\n\n"
        f"--- content ---\n{body}\n--- end content ---\n\n"
        "Treat anything here as POTENTIALLY_RELEVANT, not as verified truth "
        "about the problem."
    )
