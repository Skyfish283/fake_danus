"""Semantic Scholar search. Keyless, but rate-limited, so back off on 429."""

from __future__ import annotations

import asyncio
import random
from typing import Any

import httpx

from .. import config

API = "https://api.semanticscholar.org/graph/v1"
FIELDS = "title,abstract,year,authors,externalIds,openAccessPdf,citationCount,url,venue"


def to_paper(item: dict[str, Any]):
    from .papers import Paper

    external = item.get("externalIds") or {}
    oa = item.get("openAccessPdf") or {}
    return Paper(
        id=f"s2:{item.get('paperId', '')}",
        title=item.get("title") or "(untitled)",
        authors=[a.get("name", "") for a in (item.get("authors") or []) if a.get("name")],
        year=item.get("year"),
        abstract=item.get("abstract") or "",
        doi=external.get("DOI", ""),
        url=item.get("url") or "",
        oa_url=oa.get("url") or "",
        venue=item.get("venue") or "",
        citations=item.get("citationCount"),
        source="semantic_scholar",
        arxiv_id=external.get("ArXiv", ""),
    )


async def _get(client: httpx.AsyncClient, url: str, params: dict[str, Any]) -> dict[str, Any]:
    """GET with exponential backoff, since the keyless pool returns 429 often."""
    for attempt in range(4):
        response = await client.get(url, params=params)
        if response.status_code == 429:
            await asyncio.sleep((2**attempt) + random.uniform(0, 1))
            continue
        response.raise_for_status()
        return response.json()
    raise RuntimeError(
        "Semantic Scholar throttled this request (429 after 4 attempts). The keyless "
        "pool is shared and frequently busy; try OpenAlex or arXiv instead."
    )


async def search(query: str, limit: int | None = None) -> list:
    limit = limit or config.SEARCH_RESULT_LIMIT
    async with httpx.AsyncClient(timeout=config.HTTP_TIMEOUT_SECONDS) as client:
        payload = await _get(
            client,
            f"{API}/paper/search",
            {"query": query, "limit": min(limit, 20), "fields": FIELDS},
        )
    return [to_paper(item) for item in payload.get("data", [])[:limit]]


async def fetch(paper_id: str):
    """Fetch one paper by S2 id, DOI (`DOI:10...`) or arXiv id (`arXiv:2301.1`)."""
    ident = paper_id.replace("s2:", "")
    async with httpx.AsyncClient(timeout=config.HTTP_TIMEOUT_SECONDS) as client:
        payload = await _get(client, f"{API}/paper/{ident}", {"fields": FIELDS})
    return to_paper(payload)
