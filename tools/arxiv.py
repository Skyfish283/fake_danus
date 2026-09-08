"""arXiv search via the Atom API. Best source for maths preprints."""

from __future__ import annotations

import re
from xml.etree import ElementTree

import httpx

from .. import config

API = "https://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def _client_kwargs() -> dict:
    # The API redirects http -> https, so redirects must be followed.
    return {
        "timeout": config.HTTP_TIMEOUT_SECONDS,
        "follow_redirects": True,
        "headers": {"User-Agent": f"math-agent-prototype ({config.OPENALEX_MAILTO})"},
    }


def _text(element, path: str) -> str:
    found = element.find(path, NS)
    return " ".join((found.text or "").split()) if found is not None else ""


def _entry_to_paper(entry):
    from .papers import Paper

    raw_id = _text(entry, "atom:id")
    arxiv_id = raw_id.rsplit("/abs/", 1)[-1] if "/abs/" in raw_id else raw_id.rsplit("/", 1)[-1]
    published = _text(entry, "atom:published")
    year = int(published[:4]) if published[:4].isdigit() else None

    pdf_url = ""
    for link in entry.findall("atom:link", NS):
        if link.get("title") == "pdf" or link.get("type") == "application/pdf":
            pdf_url = link.get("href", "")
            break
    if not pdf_url and arxiv_id:
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"

    return Paper(
        id=f"arxiv:{arxiv_id}",
        title=_text(entry, "atom:title"),
        authors=[
            " ".join((name.text or "").split())
            for name in entry.findall("atom:author/atom:name", NS)
        ],
        year=year,
        abstract=_text(entry, "atom:summary"),
        doi=_text(entry, "arxiv:doi"),
        url=raw_id,
        oa_url=pdf_url,
        venue=_text(entry, "arxiv:journal_ref") or "arXiv",
        citations=None,
        source="arxiv",
        arxiv_id=arxiv_id,
    )


_STOPWORDS = {"the", "and", "for", "with", "of", "in", "on", "a", "an", "to", "is", "are"}


def _terms(query: str) -> list[str]:
    cleaned = re.sub(r"[^\w\s\-]", " ", query).lower()
    return [word for word in cleaned.split() if len(word) > 2 and word not in _STOPWORDS]


def _build_search_queries(query: str) -> list[str]:
    """arXiv wants field-prefixed boolean terms. Try AND first, then OR: an
    exact phrase match usually returns nothing for a multi-word research query."""
    terms = _terms(query)
    if not terms:
        return ["all:mathematics"]
    if len(terms) == 1:
        return [f"all:{terms[0]}"]
    return [
        " AND ".join(f"all:{term}" for term in terms[:6]),
        " OR ".join(f"all:{term}" for term in terms[:6]),
    ]


async def search(query: str, limit: int | None = None) -> list:
    limit = limit or config.SEARCH_RESULT_LIMIT
    async with httpx.AsyncClient(**_client_kwargs()) as client:
        for search_query in _build_search_queries(query):
            response = await client.get(
                API,
                params={
                    "search_query": search_query,
                    "start": 0,
                    "max_results": min(limit, 20),
                    "sortBy": "relevance",
                },
            )
            response.raise_for_status()
            entries = ElementTree.fromstring(response.text).findall("atom:entry", NS)
            if entries:
                return [_entry_to_paper(entry) for entry in entries[:limit]]
    return []


async def fetch(arxiv_id: str):
    ident = arxiv_id.replace("arxiv:", "")
    async with httpx.AsyncClient(**_client_kwargs()) as client:
        response = await client.get(API, params={"id_list": ident, "max_results": 1})
        response.raise_for_status()
        root = ElementTree.fromstring(response.text)
    entries = root.findall("atom:entry", NS)
    if not entries:
        raise LookupError(f"arXiv has no entry for {ident!r}")
    return _entry_to_paper(entries[0])
