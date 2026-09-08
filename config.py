"""Central configuration for the agentic mathematical research prototype.

Every value here is loaded from `run_config.toml` at import time, with the
previous hard-coded defaults used for anything the file omits. The rest of the
package keeps reading `config.PLANNER_MODEL`, `config.MAX_WORKER_CALLS` and so
on, so there is exactly one place that knows the file exists.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

from . import models as model_router
from .run_config import (
    CONFIG_PATH,
    EXAMPLE_PATH,
    ConfigError,
    RunConfig,
    RunOptions,
    key_fingerprint,
    load,
    options_from,
    render_redacted_toml,
    resolve_problem_text,
)

__all__ = [
    "CONFIG_PATH",
    "EXAMPLE_PATH",
    "ConfigError",
    "MissingAPIKey",
    "RUN_CONFIG",
    "RunConfig",
    "RunOptions",
    "banner_lines",
    "get_api_key",
    "key_status",
    "options_from",
    "render_redacted_toml",
    "require_api_keys",
    "resolve_problem_text",
]

PACKAGE_ROOT = Path(__file__).resolve().parent
RUNS_DIR = PACKAGE_ROOT / "runs"

# --- The run configuration --------------------------------------------------
RUN_CONFIG: RunConfig = load()

# Hand the model choices to the router, which owns the adaptive ladder and its
# cooldown state. Done here so `models` needs no imports of its own.
model_router.apply_config(
    role_models=RUN_CONFIG.models,
    ladder=RUN_CONFIG.ladder,
    cooldown_seconds=RUN_CONFIG.cooldown_seconds,
    provider=RUN_CONFIG.provider,
)

# Config roles: the names run_config.toml uses under [models], [thinking] and
# [api_keys]. The worker prompt roles (searcher, toy_example, counterexample,
# decomposer, sketcher, verifier) map onto these via
# workers.base.PROMPT_CONFIG_ROLE; the explorer/mathematician/skeptic names
# survive as the three worker API-key pools (and the baseline-B roles).
WORKER_ROLES = ("explorer", "mathematician", "skeptic", "verifier")
# The three API-key pools the six worker slots share. Verifier has no key.
WORKER_KEY_ROLES = ("explorer", "mathematician", "skeptic")

# --- Models -----------------------------------------------------------------
# Any of these may be the string "adaptive", in which case the model is chosen
# per call from the ladder in `models.py`.
PROVIDER = RUN_CONFIG.provider
PLANNER_MODEL = RUN_CONFIG.models["planner"]

WORKER_MODELS = {role: RUN_CONFIG.models[role] for role in WORKER_ROLES}

BASELINE_MODEL = RUN_CONFIG.models["baseline"]

ADAPTIVE_LADDER = RUN_CONFIG.ladder
ADAPTIVE_COOLDOWN_SECONDS = RUN_CONFIG.cooldown_seconds

# Gemini 3 Flash-family models take thinking_level (LOW/MEDIUM/HIGH) and
# ignore the legacy sampling parameters. Never combine thinking_level with
# thinking_budget: the API rejects that with a 400.
PLANNER_THINKING_LEVEL = RUN_CONFIG.thinking["planner"]

WORKER_THINKING_LEVELS = {role: RUN_CONFIG.thinking[role] for role in WORKER_ROLES}

BASELINE_THINKING_LEVEL = RUN_CONFIG.thinking["baseline"]

PLANNER_MAX_OUTPUT_TOKENS = 8192
WORKER_MAX_OUTPUT_TOKENS = 4096

# --- Budget caps ------------------------------------------------------------
# An unbounded agentic loop can spawn work indefinitely, and this model is
# billed per token, so every run is bounded on three independent axes.
MAX_PLANNER_CALLS = RUN_CONFIG.max_planner_calls
MAX_WORKER_CALLS = RUN_CONFIG.max_worker_calls
MAX_WALL_CLOCK_SECONDS = RUN_CONFIG.max_wall_clock_seconds
MAX_CONCURRENT_WORKERS = RUN_CONFIG.max_concurrent_workers

# --- Graph retrieval --------------------------------------------------------
# Workers and the planner see a slice of the graph, never the whole thing.
PLANNER_CONTEXT_NODES = 30
WORKER_CONTEXT_NODES = 12
RECENT_EVENT_TAIL = 8
MAX_NODE_CHARS_IN_CONTEXT = 1200

# --- Literature tools -------------------------------------------------------
# OpenAlex asks for a contact address to route requests to the polite pool. An
# environment variable still wins, so a shared config file need not carry it.
OPENALEX_MAILTO = os.environ.get("OPENALEX_MAILTO") or RUN_CONFIG.openalex_mailto
SEARCH_RESULT_LIMIT = RUN_CONFIG.search_result_limit
HTTP_TIMEOUT_SECONDS = 30.0
MAX_PAPER_TEXT_CHARS = 40_000

# --- Live viewer ------------------------------------------------------------
# A read-only window onto the run's own graph.json and events.jsonl, served on
# the loopback interface only.
VIEWER_ENABLED = RUN_CONFIG.viewer_enabled
VIEWER_PORT = RUN_CONFIG.viewer_port
VIEWER_OPEN_BROWSER = RUN_CONFIG.viewer_open_browser
VIEWER_POLL_MS = RUN_CONFIG.viewer_poll_ms


class MissingAPIKey(RuntimeError):
    """Raised when no API key can be found for a role."""


def _env_key_name() -> str:
    return "ZAI_API_KEY" if RUN_CONFIG.provider == "glm" else "GEMINI_API_KEY"


def _key_help_url() -> str:
    if RUN_CONFIG.provider == "glm":
        return "https://z.ai/manage-apikey/apikey-list"
    return "https://aistudio.google.com/apikey"


def resolve_api_key(role: str = "default") -> tuple[str, str]:
    """Return `(key, source)` for a role, without raising.

    A role's own key wins, then the shared `default` key, then the environment
    variable. An empty key means nothing is configured.
    """
    lookup = ["default"] if role == "default" else [model_router.config_role(role), "default"]
    for name in lookup:
        key = RUN_CONFIG.api_keys.get(name, "").strip()
        if key:
            return key, f"run_config.toml [api_keys].{name}"

    env_name = _env_key_name()
    key = (os.environ.get(env_name) or "").strip()
    if key:
        return key, env_name
    return "", "unset"


def get_api_key(role: str = "default") -> str:
    """Return the API key this role should call with, or explain how to set one."""
    key, _source = resolve_api_key(role)
    if key:
        return key
    named = "default" if role == "default" else model_router.config_role(role)
    env_name = _env_key_name()
    raise MissingAPIKey(
        f"No API key for the {named!r} role ({RUN_CONFIG.provider} provider).\n"
        f"  Set it in {CONFIG_PATH} under [api_keys] (per role, or 'default'),\n"
        "  or fall back to the environment:\n"
        f"    PowerShell (this session):  $env:{env_name} = 'your-key'\n"
        f"    PowerShell (persistent):    setx {env_name} 'your-key'\n"
        f"Get a key from {_key_help_url()}"
    )


def require_api_keys(roles: Iterable[str]) -> None:
    """Fail before any work starts if a role a run needs has no key."""
    missing = [role for role in roles if not resolve_api_key(role)[0]]
    if not missing:
        return
    env_name = _env_key_name()
    raise MissingAPIKey(
        f"No API key for: {', '.join(missing)} ({RUN_CONFIG.provider} provider).\n"
        f"  Set one per role in {CONFIG_PATH} under [api_keys], or a shared\n"
        "  [api_keys].default, or fall back to the environment:\n"
        f"    PowerShell (this session):  $env:{env_name} = 'your-key'\n"
        f"    PowerShell (persistent):    setx {env_name} 'your-key'\n"
        f"Get a key from {_key_help_url()}"
    )


def key_status(role: str = "default") -> str:
    """Human-readable key state for the run banner. Never reveals the key."""
    key, source = resolve_api_key(role)
    if not key:
        return "not set"
    return f"{key_fingerprint(key)} via {source}"


def model_status(role: str) -> str:
    """Human-readable model choice for the run banner."""
    return model_router.describe(role)


def banner_lines(roles: Iterable[str]) -> list[str]:
    """The resolved model and key for each role, safe to print."""
    lines = [
        f"config: {RUN_CONFIG.path or 'built-in defaults'}",
        f"provider: {RUN_CONFIG.provider}",
    ]
    for role in roles:
        lines.append(f"{role}: {model_status(role)} | key {key_status(role)}")
    return lines
