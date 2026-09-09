"""Thin async wrapper around the LLM API shared by the planner and workers.

Gemini and GLM share this entry point. The planner, every worker and the
baselines all bill one shared pool of API keys (`[api_keys].keys`). Each
distinct key gets its own client. A role set to "adaptive" walks the ladder in `models`, handling contention by
flavor: quota errors (429/rate-limit) rotate to another key at the same model
tier, stepping down only once every key reports the tier busy; overload
errors (503/model saturated) are confirmed on one more key and then step down
at once, since no key will work on a saturated tier. Healthy calls start on
consecutive keys round-robin, and the run summary reports how many calls each
key served.
"""

from __future__ import annotations

import asyncio
import json
import random
import time
from dataclasses import dataclass, field
from typing import Any, Callable

from google import genai
from google.genai import types

from . import config
from . import models as model_router
from .run_config import key_fingerprint

# One client per distinct API key; callers sharing a key share a client.
_gemini_clients: dict[str, genai.Client] = {}
_glm_clients: dict[str, Any] = {}

# API key -> monotonic timestamp before which we prefer other keys. A key
# that answers with a contention error is rested briefly so concurrent
# workers do not hammer a rate-limited key; a key that serves a call is
# immediately trusted again.
_key_demoted_until: dict[str, float] = {}

# Round-robin cursor: each generate() call starts at the next key, so healthy
# traffic spreads across the whole pool instead of always billing keys[0].
# (Asyncio runs one task at a time, so the read-and-bump below is atomic.)
_key_cursor = 0

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


def _gemini_client_for(key: str) -> genai.Client:
    """Return the Gemini client for this API key, created on first use."""
    client = _gemini_clients.get(key)
    if client is None:
        client = genai.Client(api_key=key)
        _gemini_clients[key] = client
    return client


def _glm_client_for(key: str) -> Any:
    """Return the Z.ai client for this API key, created on first use."""
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
    """Running tally of tokens, calls and key usage, for the run summary."""

    calls: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    by_role: dict[str, int] = field(default_factory=dict)
    by_model: dict[str, int] = field(default_factory=dict)
    by_key: dict[str, int] = field(default_factory=dict)

    def record(self, role: str, model: str, response: Any, key: str = "") -> None:
        self.calls += 1
        self.by_role[role] = self.by_role.get(role, 0) + 1
        self.by_model[model] = self.by_model.get(model, 0) + 1
        if key:
            short = key_fingerprint(key)
            self.by_key[short] = self.by_key.get(short, 0) + 1
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

    def key_breakdown(self) -> str:
        """How many calls each pooled key served, by fingerprint."""
        if not self.by_key:
            return "no keys"
        parts = sorted(self.by_key.items(), key=lambda item: -item[1])
        return ", ".join(f"{short} x{count}" for short, count in parts)

    def summary(self) -> str:
        return (
            f"{self.calls} model calls, "
            f"{self.input_tokens:,} input tokens, "
            f"{self.output_tokens:,} output tokens "
            f"({self.model_breakdown()}; keys: {self.key_breakdown()})"
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


def _key_cooldown_remaining(key: str) -> float:
    """Seconds until `key` is preferred again; 0 if it is usable now."""
    return max(0.0, _key_demoted_until.get(key, 0.0) - time.monotonic())


def _rest_key(key: str) -> None:
    """Rest a key that just reported contention, for the router's cooldown."""
    _key_demoted_until[key] = time.monotonic() + model_router.cooldown_seconds()


def _order_keys(keys: tuple[str, ...]) -> list[str]:
    """Round-robin key order for one call: usable keys first, rotated.

    Each call starts at the next pool position, so consecutive healthy calls
    bill K1, K2, K3, ... in turn. Rested keys always go last
    (soonest-available first) regardless of the cursor.
    """
    global _key_cursor
    ready = [key for key in keys if _key_cooldown_remaining(key) <= 0]
    resting = sorted(
        (key for key in keys if _key_cooldown_remaining(key) > 0),
        key=_key_cooldown_remaining,
    )
    if ready:
        start = _key_cursor % len(ready)
        _key_cursor += 1
        ready = ready[start:] + ready[:start]
    return ready + resting


def _short_key(key: str) -> str:
    """Fingerprint for log lines; the key itself never reaches a log."""
    return key_fingerprint(key)


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
    system_instruction: str | None = None,
    thinking_level: str | None = None,
    max_output_tokens: int | None = None,
    response_schema: Any | None = None,
    max_attempts: int = 4,
) -> str:
    """Run one async model call and return its text.

    `model` may be omitted or set to "adaptive", in which case the role's
    configured choice decides; a concrete ID pins the call to that model.
    Every call bills the shared `[api_keys].keys` pool, starting each call on
    the next key round-robin so healthy traffic spreads across the pool.
    Contention is handled by flavor: quota errors (429/rate-limit) rotate to
    another key at the same model tier, while overload errors (503/model
    saturated) are confirmed on one more key and then step down the ladder
    at once, since no key will work on a saturated tier. Only once every key
    has reported the tier busy does a quota-hit call step down.
    `max_attempts` bounds the backoff retries for transient (non-contention)
    errors on one key before moving to the next key.
    """
    keys = config.api_key_pool()
    if not keys:
        config.require_api_keys()
    use_glm = model_router.provider() == "glm"
    gemini_cfg: types.GenerateContentConfig | None = None
    if not use_glm:
        gemini_cfg = _build_config(
            system_instruction=system_instruction,
            thinking_level=thinking_level,
            max_output_tokens=max_output_tokens,
            response_schema=response_schema,
        )

    candidates = model_router.candidates(role, model)
    # One rotation per call, shared by every tier: consecutive calls start on
    # consecutive keys, and a tier that fails on one key resumes on the next.
    key_order = _order_keys(keys)
    last_error: Exception | None = None
    for index, candidate in enumerate(candidates):
        if index:
            _note(f"{role}: falling back to {candidate}")
        model_saw_contention = False
        quota_hits = 0
        overload_hits = 0

        for key in key_order:
            short = _short_key(key)
            if use_glm:
                client: Any = _glm_client_for(key)
            else:
                assert gemini_cfg is not None
                client = _gemini_client_for(key)

            step_down = False
            for attempt in range(max_attempts):
                try:
                    if use_glm:
                        response = await asyncio.to_thread(
                            _glm_create,
                            client,
                            candidate=candidate,
                            prompt=prompt,
                            system_instruction=system_instruction,
                            thinking_level=thinking_level,
                            max_output_tokens=max_output_tokens,
                            response_schema=response_schema,
                        )
                        text = _glm_message_text(response)
                    else:
                        response = await _call_gemini(
                            client=client,
                            candidate=candidate,
                            prompt=prompt,
                            cfg=gemini_cfg,
                        )
                        text = (response.text or "").strip()
                except asyncio.CancelledError:
                    raise
                except Exception as exc:  # noqa: BLE001 - surfaced to the caller below
                    last_error = exc
                    kind = model_router.contention_kind(exc)
                    if kind == "quota":
                        # This key (or its project) is throttled: rest it and
                        # try another key on the same tier.
                        quota_hits += 1
                        model_saw_contention = True
                        _rest_key(key)
                        _note(
                            f"{role}: {candidate} quota-exhausted on key {short}; "
                            "trying another key"
                        )
                        break  # next key, same model tier
                    if kind == "overload":
                        # The tier itself is saturated: confirm on one more
                        # key, then step down instead of grinding every key.
                        # The key is fine, so it is not rested.
                        overload_hits += 1
                        model_saw_contention = True
                        if overload_hits >= 2:
                            _note(
                                f"{role}: {candidate} overloaded on "
                                f"{overload_hits} keys; stepping down"
                            )
                            step_down = True
                            break  # out of the key loop -> next tier
                        _note(
                            f"{role}: {candidate} overloaded on key {short}; "
                            "confirming on one more key"
                        )
                        break  # next key, same model tier
                    if not _is_retryable(exc):
                        raise
                    if attempt == max_attempts - 1:
                        break  # out of attempts on this key; try the next one
                    await asyncio.sleep((2**attempt) + random.uniform(0, 1))
                    continue

                USAGE.record(role, candidate, response, key)
                _key_demoted_until.pop(key, None)
                if text:
                    return text

                finish = _empty_finish_reason(response)
                raise RuntimeError(
                    f"Model returned no text from {candidate} "
                    f"(finish_reason={finish or 'unknown'})"
                )

            if step_down:
                break  # overload confirmed: skip the rest of this tier

        if model_saw_contention:
            cooldown = model_router.mark_contended(candidate)
            if quota_hits >= len(key_order) and overload_hits == 0:
                _note(
                    f"{candidate} demoted for {cooldown:.0f}s; every key reports "
                    "quota exhaustion — the keys likely share one project quota, "
                    "so rotation cannot help; stepping down / waiting is the remedy"
                )
            else:
                _note(f"{candidate} is busy; demoted for {cooldown:.0f}s")

    tried = " -> ".join(candidates)
    label = "GLM" if use_glm else "Gemini"
    raise RuntimeError(
        f"{label} call failed after trying {tried} "
        f"on {len(keys)} pooled key(s): {last_error}"
    )
