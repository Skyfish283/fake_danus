"""Thin async wrapper around the LLM API shared by the planner and workers.

Gemini and GLM share this entry point. Each distinct API key gets its own
client, so roles (or worker slots) configured with different keys do not share
a quota. `key_role` can bill a different pool than the mathematical `role`
(flex slots sharing a specialised worker's key). A role set to "adaptive"
walks the ladder in `models`: a busy model is demoted and the call steps down
to the next one immediately, rather than sitting in backoff.
"""

from __future__ import annotations

import asyncio
import json
import random
from dataclasses import dataclass, field
from typing import Any, Callable

from google import genai
from google.genai import types

from . import config
from . import models as model_router

# One client per distinct API key; roles sharing a key share a client.
_gemini_clients: dict[str, genai.Client] = {}
_glm_clients: dict[str, Any] = {}

# GLM-4.7-Flash does not take reasoning_effort (that is GLM-5.2+).
# LOW turns thinking off; MEDIUM and HIGH leave it on.
_GLM_TIMEOUT_SECONDS = 300.0

# Set by an entry point so model switches reach log.txt instead of vanishing.
_note_sink: Callable[[str, str], None] | None = None

_RETRYABLE_MARKERS = (
    "500",
    "502",
    "504",
    "deadline",
    "timeout",
    "internal error",
)


def set_note_sink(sink: Callable[[str, str], None] | None) -> None:
    """Route client-level notices (model demotions, retries) to a run log."""
    global _note_sink
    _note_sink = sink


def _note(message: str) -> None:
    if _note_sink is not None:
        _note_sink("System", message)


def get_client(role: str = "default") -> genai.Client:
    """Return the Gemini client for this role's API key, created on first use."""
    key = config.get_api_key(role)
    client = _gemini_clients.get(key)
    if client is None:
        client = genai.Client(api_key=key)
        _gemini_clients[key] = client
    return client


def _get_glm_client(role: str = "default") -> Any:
    """Return the Z.ai client for this role's API key, created on first use."""
    key = config.get_api_key(role)
    client = _glm_clients.get(key)
    if client is not None:
        return client
    try:
        import httpx
        from zai import ZaiClient
    except ImportError as exc:
        raise RuntimeError(
            "GLM provider requires the zai-sdk package. Install it with:\n"
            "  pip install zai-sdk"
        ) from exc
    client = ZaiClient(
        api_key=key,
        timeout=httpx.Timeout(timeout=_GLM_TIMEOUT_SECONDS, connect=8.0),
    )
    _glm_clients[key] = client
    return client


@dataclass
class Usage:
    """Running tally of tokens and calls, for the run summary."""

    calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    by_role: dict[str, int] = field(default_factory=dict)
    by_model: dict[str, int] = field(default_factory=dict)

    def record(self, role: str, model: str, response: Any) -> None:
        self.calls += 1
        self.by_role[role] = self.by_role.get(role, 0) + 1
        self.by_model[model] = self.by_model.get(model, 0) + 1
        meta = getattr(response, "usage_metadata", None)
        if meta is not None:
            self.input_tokens += getattr(meta, "prompt_token_count", 0) or 0
            # Thinking tokens are billed as output, so fold them in.
            self.output_tokens += getattr(meta, "candidates_token_count", 0) or 0
            self.output_tokens += getattr(meta, "thoughts_token_count", 0) or 0
            return
        usage = getattr(response, "usage", None)
        if usage is not None:
            self.input_tokens += getattr(usage, "prompt_tokens", 0) or 0
            self.output_tokens += getattr(usage, "completion_tokens", 0) or 0

    def model_breakdown(self) -> str:
        """Which models actually served the calls; adaptive runs need this."""
        if not self.by_model:
            return "no calls"
        parts = sorted(self.by_model.items(), key=lambda item: -item[1])
        return ", ".join(f"{model} x{count}" for model, count in parts)

    def summary(self) -> str:
        return (
            f"{self.calls} model calls, "
            f"{self.input_tokens:,} input tokens, "
            f"{self.output_tokens:,} output tokens "
            f"({self.model_breakdown()})"
        )


USAGE = Usage()


def _build_config(
    *,
    system_instruction: str | None,
    thinking_level: str | None,
    max_output_tokens: int | None,
    response_schema: Any | None,
) -> types.GenerateContentConfig:
    kwargs: dict[str, Any] = {}
    if system_instruction:
        kwargs["system_instruction"] = system_instruction
    if max_output_tokens:
        kwargs["max_output_tokens"] = max_output_tokens
    if response_schema is not None:
        kwargs["response_mime_type"] = "application/json"
        kwargs["response_schema"] = response_schema
    if thinking_level:
        kwargs["thinking_config"] = types.ThinkingConfig(thinking_level=thinking_level)
    # Deliberately no temperature/top_p/top_k: Gemini 3 Flash models ignore them.
    return types.GenerateContentConfig(**kwargs)


def _is_retryable(error: Exception) -> bool:
    if model_router.is_contention_error(error):
        return True
    text = f"{type(error).__name__} {error}".lower()
    return any(marker in text for marker in _RETRYABLE_MARKERS)


def _glm_system_text(system_instruction: str | None, response_schema: Any | None) -> str:
    parts: list[str] = []
    if system_instruction and system_instruction.strip():
        parts.append(system_instruction.strip())
    if response_schema is not None:
        try:
            schema_text = json.dumps(response_schema, ensure_ascii=False)
        except TypeError:
            schema_text = str(response_schema)
        parts.append(
            "Return a JSON object matching this schema, and nothing else:\n" + schema_text
        )
    return "\n\n".join(parts)


def _glm_message_text(response: Any) -> str:
    choices = getattr(response, "choices", None) or []
    if not choices:
        return ""
    message = getattr(choices[0], "message", None)
    if message is None:
        return ""
    content = getattr(message, "content", None)
    return (content or "").strip()


def _empty_finish_reason(response: Any) -> str:
    finish = ""
    response_candidates = getattr(response, "candidates", None) or []
    if response_candidates:
        finish = str(getattr(response_candidates[0], "finish_reason", "") or "")
    if finish:
        return finish
    choices = getattr(response, "choices", None) or []
    if choices:
        return str(getattr(choices[0], "finish_reason", "") or "")
    return "unknown"


async def _call_gemini(
    *,
    client: genai.Client,
    candidate: str,
    prompt: str,
    cfg: types.GenerateContentConfig,
) -> Any:
    return await client.aio.models.generate_content(
        model=candidate, contents=prompt, config=cfg
    )


def _glm_create(
    client: Any,
    *,
    candidate: str,
    prompt: str,
    system_instruction: str | None,
    thinking_level: str | None,
    max_output_tokens: int | None,
    response_schema: Any | None,
) -> Any:
    thinking_type = "disabled" if (thinking_level or "HIGH").upper() == "LOW" else "enabled"
    messages: list[dict[str, str]] = []
    system_text = _glm_system_text(system_instruction, response_schema)
    if system_text:
        messages.append({"role": "system", "content": system_text})
    messages.append({"role": "user", "content": prompt})
    kwargs: dict[str, Any] = {
        "model": candidate,
        "messages": messages,
        "thinking": {"type": thinking_type},
    }
    if max_output_tokens:
        kwargs["max_tokens"] = max_output_tokens
    if response_schema is not None:
        kwargs["response_format"] = {"type": "json_object"}
    return client.chat.completions.create(**kwargs)


async def generate(
    prompt: str,
    *,
    role: str,
    model: str | None = None,
    key_role: str | None = None,
    system_instruction: str | None = None,
    thinking_level: str | None = None,
    max_output_tokens: int | None = None,
    response_schema: Any | None = None,
    max_attempts: int = 4,
) -> str:
    """Run one async model call and return its text.

    `model` may be omitted or set to "adaptive", in which case the role's
    configured choice decides; a concrete ID pins the call to that model.
    `key_role` selects which [api_keys] pool to bill; omitted, it follows `role`.
    Model choice, thinking, and usage tally still follow `role`.
    """
    billed = key_role or role
    use_glm = model_router.provider() == "glm"
    gemini_client: genai.Client | None = None
    glm_client: Any = None
    gemini_cfg: types.GenerateContentConfig | None = None
    if use_glm:
        glm_client = _get_glm_client(billed)
    else:
        gemini_client = get_client(billed)
        gemini_cfg = _build_config(
            system_instruction=system_instruction,
            thinking_level=thinking_level,
            max_output_tokens=max_output_tokens,
            response_schema=response_schema,
        )

    candidates = model_router.candidates(role, model)
    last_error: Exception | None = None
    for index, candidate in enumerate(candidates):
        lower_rung_available = index < len(candidates) - 1
        if index:
            _note(f"{role}: falling back to {candidate}")

        for attempt in range(max_attempts):
            try:
                if use_glm:
                    response = await asyncio.to_thread(
                        _glm_create,
                        glm_client,
                        candidate=candidate,
                        prompt=prompt,
                        system_instruction=system_instruction,
                        thinking_level=thinking_level,
                        max_output_tokens=max_output_tokens,
                        response_schema=response_schema,
                    )
                    text = _glm_message_text(response)
                else:
                    assert gemini_client is not None and gemini_cfg is not None
                    response = await _call_gemini(
                        client=gemini_client,
                        candidate=candidate,
                        prompt=prompt,
                        cfg=gemini_cfg,
                    )
                    text = (response.text or "").strip()
            except asyncio.CancelledError:
                raise
            except Exception as exc:  # noqa: BLE001 - surfaced to the caller below
                last_error = exc
                if model_router.is_contention_error(exc):
                    cooldown = model_router.mark_contended(candidate)
                    _note(f"{candidate} is busy; demoted for {cooldown:.0f}s")
                    if lower_rung_available:
                        break  # step down the ladder instead of waiting
                if not _is_retryable(exc):
                    raise
                if attempt == max_attempts - 1:
                    break  # out of attempts on this model; try the next one
                await asyncio.sleep((2**attempt) + random.uniform(0, 1))
                continue

            USAGE.record(role, candidate, response)
            if text:
                return text

            finish = _empty_finish_reason(response)
            raise RuntimeError(
                f"Model returned no text from {candidate} "
                f"(finish_reason={finish or 'unknown'})"
            )

    tried = " -> ".join(candidates)
    label = "GLM" if use_glm else "Gemini"
    raise RuntimeError(f"{label} call failed after trying {tried}: {last_error}")
