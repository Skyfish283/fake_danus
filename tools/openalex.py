"""OpenAlex search: the primary literature tool. Free, keyless, no auth."""

from __future__ import annotations

from typing import Any

import httpx

from .. import config

API = "https://api.openalex.org/works"


def _abstract_from_inverted_index(index: dict[str, list[int]] | None) -> str:
    """OpenAlex stores abstracts as {word: [positions]}; put them back in order."""
    if not index:
        return ""
    positions: list[tuple[int, str]] = []
    for word, spots in index.items():
        for spot in spots:
            positions.append((spot, word))
    positions.sort()
    return " ".join(word for _, word in positions)


def _authors(work: dict[str, Any]) -> list[str]:
    names = []
    for authorship in work.get("authorships") or []:
        author = (authorship or {}).get("author") or {}
        name = author.get("display_name")
        if name:
            names.append(name)
    return names


def _short_id(openalex_id: str) -> str:
    return (openalex_id or "").rsplit("/", 1)[-1]


def to_paper(work: dict[str, Any]):
    from .papers import Paper

    open_access = work.get("open_access") or {}
    location = work.get("best_oa_location") or work.get("primary_location") or {}
    return Paper(
        id=f"openalex:{_short_id(work.get('id', ''))}",
        title=work.get("display_name") or work.get("title") or "(untitled)",
        authors=_authors(work),
        year=work.get("publication_year"),
        abstract=_abstract_from_inverted_index(work.get("abstract_inverted_index")),
        doi=(work.get("doi") or "").replace("https://doi.org/", ""),
        url=work.get("id") or "",
        oa_url=open_access.get("oa_url") or location.get("pdf_url") or "",
        venue=(location.get("source") or {}).get("display_name") or "",
        citations=work.get("cited_by_count"),
        source="openalex",
    )


async def search(query: str, limit: int | None = None) -> list:
    """Search OpenAlex works, normalised to Paper.

    Searching title and abstract is far more precise than the default `search`,
    which also indexes full text and tends to surface highly cited reviews that
    merely mention the terms. The broad search is kept as a fallback.
    """
    limit = limit or config.SEARCH_RESULT_LIMIT
    per_page = min(max(limit, 1), 25)
    attempts = (
        {"filter": f"title_and_abstract.search:{query}", "per-page": per_page},
        {"search": query, "per-page": per_page},
    )

    collected: dict[str, Any] = {}
    async with httpx.AsyncClient(timeout=config.HTTP_TIMEOUT_SECONDS) as client:
        for params in attempts:
            response = await client.get(
                API, params={**params, "mailto": config.OPENALEX_MAILTO}
            )
            if response.status_code >= 400:
                continue
            for work in response.json().get("results", []):
                collected.setdefault(work.get("id", ""), work)
            # The precise search often returns only a handful; top it up with
            # the broader one rather than handing back a single paper.
            if len(collected) >= max(3, limit):
                break

    return [to_paper(work) for work in list(collected.values())[:limit]]


async def fetch(openalex_id: str):
    """Fetch a single work by OpenAlex id (with or without the W prefix path)."""
    ident = _short_id(openalex_id.replace("openalex:", ""))
    async with httpx.AsyncClient(timeout=config.HTTP_TIMEOUT_SECONDS) as client:
        response = await client.get(
            f"{API}/{ident}", params={"mailto": config.OPENALEX_MAILTO}
        )
        response.raise_for_status()
        return to_paper(response.json())
