"""Which model serves a call, including the adaptive fallback ladder.

A role may be pinned to one model ID or set to "adaptive". Adaptive roles walk
an ordered ladder from strongest to cheapest: whenever a model answers with a
contention error the caller reports it here, that model is demoted for a
cooldown, and the next call steps down to the one below. Once the cooldown
lapses the better model returns to the front of the ladder and gets probed
again, so a run recovers instead of staying on the weakest model forever.

This module deliberately imports nothing else from the package: `config` pushes
the loaded run configuration in via `apply_config`, which keeps the import
graph acyclic (run_config -> models, config -> run_config).
"""

from __future__ import annotations

import time
from typing import Iterable, Sequence

# Roles that can be configured independently in run_config.toml under
# [models] and [thinking]. All autonomous workers share the "worker" role.
ROLES = ("planner", "worker", "baseline")

# [api_keys] names for the autonomous worker architecture.
KEY_ROLES = ("planner", "worker", "baseline")

# Whole-run switch in [models].provider. Mixing providers in one run is not allowed.
PROVIDERS = ("gemini", "glm")
DEFAULT_PROVIDER = "gemini"

# Gemini Flash-family IDs. Edit here if Google renames one.
GEMINI_MODELS = (
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite",
)

# Z.AI GLM IDs. Edit here if Z.AI renames one.
GLM_MODELS = (
    "glm-4.7-flash",
)

# Union of every ID the system will call, across providers.
KNOWN_MODELS = GEMINI_MODELS + GLM_MODELS

# Sentinel a role can be set to instead of a concrete model ID.
ADAPTIVE = "adaptive"

DEFAULT_GEMINI_LADDER: tuple[str, ...] = GEMINI_MODELS
DEFAULT_GLM_LADDER: tuple[str, ...] = GLM_MODELS
# Backward-compatible alias: Gemini is the default provider.
DEFAULT_LADDER: tuple[str, ...] = DEFAULT_GEMINI_LADDER

DEFAULT_GEMINI_MODEL = "gemini-3.5-flash-lite"
DEFAULT_GLM_MODEL = "glm-4.7-flash"
DEFAULT_MODEL = DEFAULT_GEMINI_MODEL
DEFAULT_COOLDOWN_SECONDS = 180.0

# Gemini-only alias kept so older imports still resolve. Prefer choices_for().
MODEL_CHOICES = GEMINI_MODELS + (ADAPTIVE,)

_provider: str = DEFAULT_PROVIDER
_role_models: dict[str, str] = {role: DEFAULT_MODEL for role in ROLES}
_ladder: tuple[str, ...] = DEFAULT_LADDER
_cooldown_seconds: float = DEFAULT_COOLDOWN_SECONDS

# model ID -> monotonic timestamp before which we should not prefer it.
_demoted_until: dict[str, float] = {}

# Substrings that mean "this model is busy right now", as opposed to a bad
# request, which no amount of stepping down would fix.
_CONTENTION_MARKERS = (
    "429",
    "503",
    "resource_exhausted",
    "resource exhausted",
    "unavailable",
    "overloaded",
    "quota",
    "rate limit",
    "too many requests",
)

_ROLE_ALIASES = {
    "baseline_a": "baseline",
    "baseline_b_synthesis": "baseline",
    "smoke_test": "planner",
    # Flex slots share a specialised worker's key pool, never the planner key.
    "flex_1": "explorer",
    "flex_2": "mathematician",
    "flex_3": "skeptic",
    "flex_4": "explorer",
    "flex_5": "mathematician",
    "flex_6": "skeptic",
}


def known_models(provider: str = DEFAULT_PROVIDER) -> tuple[str, ...]:
    """Model IDs this provider will actually call."""
    if provider == "glm":
        return GLM_MODELS
    return GEMINI_MODELS


def choices_for(provider: str = DEFAULT_PROVIDER) -> tuple[str, ...]:
    """known_models plus the adaptive sentinel."""
    return known_models(provider) + (ADAPTIVE,)


def default_model(provider: str = DEFAULT_PROVIDER) -> str:
    return DEFAULT_GLM_MODEL if provider == "glm" else DEFAULT_GEMINI_MODEL


def default_ladder(provider: str = DEFAULT_PROVIDER) -> tuple[str, ...]:
    return DEFAULT_GLM_LADDER if provider == "glm" else DEFAULT_GEMINI_LADDER


def apply_config(
    *,
    role_models: dict[str, str] | None = None,
    ladder: Sequence[str] | None = None,
    cooldown_seconds: float | None = None,
    provider: str | None = None,
) -> None:
    """Install the loaded run configuration. Called once, from `config`."""
    global _ladder, _cooldown_seconds, _provider
    if provider:
        _provider = provider
    if role_models:
        _role_models.update({role: role_models[role] for role in role_models if role in ROLES})
    if ladder:
        _ladder = tuple(ladder)
    if cooldown_seconds is not None:
        _cooldown_seconds = float(cooldown_seconds)


def provider() -> str:
    """The whole-run provider: gemini or glm."""
    return _provider


def config_role(call_role: str) -> str:
    """Map a call-site role string onto one of the configurable roles.

    Call sites use finer-grained names than the config does: `baseline_a`,
    `baseline_b_explorer`, `smoke_test`, `flex_1` and so on. Flex slots map
    onto the worker-key pool they share, not onto the planner.
    """
    role = (call_role or "").strip().lower()
    if role in ROLES:
        return role
    if role in _ROLE_ALIASES:
        return _ROLE_ALIASES[role]
    if role.startswith("baseline_b_"):
        # Arm B's workers run the worker models, so they use the worker's key.
        inner = role[len("baseline_b_") :]
        return inner if inner in ROLES else "baseline"
    if role.startswith("baseline"):
        return "baseline"
    return "planner"


def model_for(call_role: str) -> str:
    """The configured choice for a role: a model ID, or "adaptive"."""
    return _role_models.get(config_role(call_role), default_model(_provider))


def is_demoted(model: str) -> bool:
    return _demoted_until.get(model, 0.0) > time.monotonic()


def demoted_for(model: str) -> float:
    """Seconds until `model` is preferred again; 0 if it is available now."""
    return max(0.0, _demoted_until.get(model, 0.0) - time.monotonic())


def mark_contended(model: str) -> float:
    """Demote a busy model and return how long it will stay demoted."""
    _demoted_until[model] = time.monotonic() + _cooldown_seconds
    return _cooldown_seconds


def is_contention_error(error: BaseException) -> bool:
    """True when the failure means "busy", not "wrong request"."""
    text = f"{type(error).__name__} {error}".lower()
    return any(marker in text for marker in _CONTENTION_MARKERS)


def candidates(call_role: str, explicit_model: str | None = None) -> list[str]:
    """Models to try for this call, best available first.

    A pinned model yields a single-entry list. An adaptive role yields the whole
    ladder with any model still in cooldown pushed to the back rather than
    dropped, so there is always something left to call.
    """
    choice = (explicit_model or "").strip() or model_for(call_role)
    if choice != ADAPTIVE:
        return [choice]

    ready = [m for m in _ladder if not is_demoted(m)]
    busy = sorted((m for m in _ladder if is_demoted(m)), key=demoted_for)
    return ready + busy or [default_model(_provider)]


def describe(call_role: str) -> str:
    """One-line description of a role's model choice, for the run banner."""
    choice = model_for(call_role)
    if choice != ADAPTIVE:
        return choice
    return f"adaptive ({' -> '.join(_ladder)})"


def ladder() -> tuple[str, ...]:
    return _ladder


def cooldown_seconds() -> float:
    return _cooldown_seconds


def reset_demotions(models: Iterable[str] | None = None) -> None:
    """Clear cooldown state; used by tests and between arms of a run."""
    if models is None:
        _demoted_until.clear()
        return
    for model in models:
        _demoted_until.pop(model, None)
