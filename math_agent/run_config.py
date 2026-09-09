"""Reads run_config.toml, the single file that describes one run.

Parsing and validation only: nothing here touches the network, the graph, or
global state. `config` imports this once and exposes the result through its own
constants, so the rest of the package keeps reading `config.PLANNER_MODEL` and
friends as before.
"""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Sequence

from .models import (
    ADAPTIVE,
    DEFAULT_LADDER,
    KEY_ROLES,
    PROVIDERS,
    ROLES,
    choices_for,
    default_ladder,
    default_model,
    known_models,
)

PACKAGE_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = PACKAGE_ROOT / "run_config.toml"
EXAMPLE_PATH = PACKAGE_ROOT / "run_config.example.toml"

MODES = ("main", "baseline_a", "baseline_b", "baselines_both")
THINKING_LEVELS = ("LOW", "MEDIUM", "HIGH")

DEFAULT_MODELS: dict[str, str] = {role: "gemini-3.5-flash-lite" for role in ROLES}
DEFAULT_THINKING: dict[str, str] = {
    "planner": "HIGH",
    "worker": "MEDIUM",
    "baseline": "HIGH",
}

_SECTIONS = {
    "run": ("mode", "problem", "problem_file", "tag", "resume"),
    "budget": (
        "max_planner_calls",
        "max_worker_calls",
        "max_wall_clock_seconds",
        "max_concurrent_workers",
    ),
    "models": ("provider",) + ROLES,
    "thinking": ROLES,
    "api_keys": ("default",) + KEY_ROLES,
    "adaptive": ("ladder", "cooldown_seconds"),
    "literature": ("openalex_mailto", "search_result_limit"),
    "viewer": ("enabled", "port", "open_browser", "poll_ms"),
}


class ConfigError(RuntimeError):
    """Raised for a run_config.toml the system cannot honour."""


@dataclass(frozen=True)
class RunConfig:
    """Everything run_config.toml can say, with defaults for anything omitted."""

    mode: str = "main"
    problem: str = ""
    problem_file: str = ""
    tag: str = ""
    resume: str = ""

    max_planner_calls: int = 40
    max_worker_calls: int = 30
    max_wall_clock_seconds: float = 30 * 60
    max_concurrent_workers: int = 6

    provider: str = "gemini"
    models: dict[str, str] = field(default_factory=lambda: dict(DEFAULT_MODELS))
    thinking: dict[str, str] = field(default_factory=lambda: dict(DEFAULT_THINKING))
    api_keys: dict[str, str] = field(default_factory=dict)

    ladder: tuple[str, ...] = DEFAULT_LADDER
    cooldown_seconds: float = 180.0

    openalex_mailto: str = "math-agent-prototype@example.com"
    search_result_limit: int = 8

    viewer_enabled: bool = True
    viewer_port: int = 8765
    viewer_open_browser: bool = True
    viewer_poll_ms: int = 1000

    path: Path | None = None
    warnings: tuple[str, ...] = ()

    def uses_adaptive(self) -> bool:
        return any(choice == ADAPTIVE for choice in self.models.values())

    def roles_in_use(self) -> tuple[str, ...]:
        """Roles a run in this mode will actually call.

        For main mode: planner and worker roles are used.
        """
        if self.mode == "main":
            return ("planner", "worker")
        if self.mode == "baseline_a":
            return ("baseline",)
        return KEY_ROLES


@dataclass
class RunOptions:
    """The resolved instructions one entry point needs to start a run."""

    mode: str = "main"
    problem: str = ""
    tag: str = ""
    resume: str = ""
    max_planner_calls: int = 40
    max_worker_calls: int = 30
    max_seconds: float = 30 * 60

    @property
    def arm(self) -> str:
        """Baseline arm label, as `baselines.py` reports it."""
        if self.mode == "baseline_a":
            return "A"
        if self.mode == "baseline_b":
            return "B"
        return "both"

    @property
    def arms(self) -> tuple[str, ...]:
        if self.mode == "baseline_a":
            return ("A",)
        if self.mode == "baseline_b":
            return ("B",)
        return ("A", "B")


# -- loading -----------------------------------------------------------------


def load(path: str | Path | None = None) -> RunConfig:
    """Load and validate the run config, falling back to built-in defaults."""
    path = Path(path) if path else CONFIG_PATH
    if not path.exists():
        return RunConfig(
            warnings=(
                f"{path.name} not found; using built-in defaults and the "
                f"GEMINI_API_KEY environment variable. Copy {EXAMPLE_PATH.name} "
                f"to {path.name} to configure a run.",
            )
        )

    try:
        raw = tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"{path} is not valid TOML: {exc}") from exc
    except OSError as exc:
        raise ConfigError(f"could not read {path}: {exc}") from exc

    warnings: list[str] = []
    for name in raw:
        if name not in _SECTIONS:
            warnings.append(f"unknown section [{name}] ignored")

    run = _table(raw, "run", warnings)
    budget = _table(raw, "budget", warnings)
    models = _table(raw, "models", warnings)
    thinking = _table(raw, "thinking", warnings)
    api_keys = _table(raw, "api_keys", warnings)
    adaptive = _table(raw, "adaptive", warnings)
    literature = _table(raw, "literature", warnings)
    viewer = _table(raw, "viewer", warnings)

    defaults = RunConfig()

    mode = _text(run, "mode", defaults.mode, warnings, "run").lower()
    if mode not in MODES:
        raise ConfigError(
            f"[run] mode = {mode!r} is not recognised. Choose one of: {', '.join(MODES)}."
        )

    provider = _read_provider(models, warnings)

    config = RunConfig(
        mode=mode,
        problem=_text(run, "problem", "", warnings, "run"),
        problem_file=_text(run, "problem_file", "", warnings, "run"),
        tag=_text(run, "tag", "", warnings, "run"),
        resume=_text(run, "resume", "", warnings, "run"),
        max_planner_calls=_whole(
            budget, "max_planner_calls", defaults.max_planner_calls, warnings, "budget"
        ),
        max_worker_calls=_whole(
            budget, "max_worker_calls", defaults.max_worker_calls, warnings, "budget"
        ),
        max_wall_clock_seconds=_number(
            budget,
            "max_wall_clock_seconds",
            defaults.max_wall_clock_seconds,
            warnings,
            "budget",
        ),
        max_concurrent_workers=_whole(
            budget,
            "max_concurrent_workers",
            defaults.max_concurrent_workers,
            warnings,
            "budget",
        ),
        provider=provider,
        models=_read_models(models, provider, warnings),
        thinking=_read_thinking(thinking, warnings),
        api_keys=_read_api_keys(api_keys, warnings),
        ladder=_read_ladder(adaptive, provider, warnings),
        cooldown_seconds=_number(
            adaptive, "cooldown_seconds", defaults.cooldown_seconds, warnings, "adaptive"
        ),
        openalex_mailto=_text(
            literature, "openalex_mailto", defaults.openalex_mailto, warnings, "literature"
        ),
        search_result_limit=_whole(
            literature, "search_result_limit", defaults.search_result_limit, warnings, "literature"
        ),
        viewer_enabled=_flag(viewer, "enabled", defaults.viewer_enabled, warnings, "viewer"),
        viewer_port=_port(viewer, "port", defaults.viewer_port, warnings, "viewer"),
        viewer_open_browser=_flag(
            viewer, "open_browser", defaults.viewer_open_browser, warnings, "viewer"
        ),
        viewer_poll_ms=_whole(viewer, "poll_ms", defaults.viewer_poll_ms, warnings, "viewer"),
        path=path,
        warnings=tuple(warnings),
    )
    return config


def options_from(config: RunConfig) -> RunOptions:
    """Turn a RunConfig into the options an entry point runs with."""
    return RunOptions(
        mode=config.mode,
        problem=resolve_problem_text(config),
        tag=config.tag,
        resume=config.resume,
        max_planner_calls=config.max_planner_calls,
        max_worker_calls=config.max_worker_calls,
        max_seconds=config.max_wall_clock_seconds,
    )


def resolve_problem_text(config: RunConfig) -> str:
    """The problem statement, preferring `problem_file` when one is given."""
    if config.problem_file:
        path = Path(config.problem_file)
        if not path.is_absolute():
            # Relative to the package, so the same config works from any cwd.
            candidate = PACKAGE_ROOT / path
            path = candidate if candidate.exists() else path
        try:
            return path.read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise ConfigError(f"[run] problem_file could not be read: {exc}") from exc
    return config.problem.strip()


# -- reporting ---------------------------------------------------------------


def key_fingerprint(key: str) -> str:
    """Enough of a key to tell two apart, never enough to use it."""
    if not key:
        return "not set"
    return f"set (...{key[-4:]})" if len(key) > 4 else "set"


def render_redacted_toml(config: RunConfig, options: RunOptions | None = None) -> str:
    """The effective config as TOML, with API keys reduced to a marker.

    Written into each run directory so a result stays reproducible without ever
    copying a secret into the output. Pass the run's `options` so command-line
    overrides are recorded rather than the file's own values.
    """
    options = options or options_from(config)
    lines = [
        "# Effective configuration for this run. API keys are redacted.",
        f"# Source: {config.path or 'built-in defaults'}",
        "",
        "[run]",
        f'mode = "{options.mode}"',
        f"problem = {_toml_string(options.problem)}",
        f'tag = "{options.tag}"',
        f'resume = "{options.resume}"',
        "",
        "[budget]",
        f"max_planner_calls = {options.max_planner_calls}",
        f"max_worker_calls = {options.max_worker_calls}",
        f"max_wall_clock_seconds = {options.max_seconds:g}",
        f"max_concurrent_workers = {config.max_concurrent_workers}",
        "",
        "[models]",
        f'provider = "{config.provider}"',
    ]
    lines += [f'{role} = "{config.models[role]}"' for role in ROLES]
    lines += ["", "[thinking]"]
    lines += [f'{role} = "{config.thinking[role]}"' for role in ROLES]
    lines += ["", "[api_keys]"]
    lines += [
        f'{role} = "{key_fingerprint(config.api_keys.get(role, ""))}"'
        for role in ("default",) + KEY_ROLES
    ]
    lines += [
        "",
        "[adaptive]",
        "ladder = [" + ", ".join(f'"{m}"' for m in config.ladder) + "]",
        f"cooldown_seconds = {config.cooldown_seconds:g}",
        "",
        "[literature]",
        f'openalex_mailto = "{config.openalex_mailto}"',
        f"search_result_limit = {config.search_result_limit}",
        "",
        "[viewer]",
        f"enabled = {str(config.viewer_enabled).lower()}",
        f"port = {config.viewer_port}",
        f"open_browser = {str(config.viewer_open_browser).lower()}",
        f"poll_ms = {config.viewer_poll_ms}",
        "",
    ]
    return "\n".join(lines)


# -- primitives --------------------------------------------------------------


def _table(raw: dict[str, Any], name: str, warnings: list[str]) -> dict[str, Any]:
    section = raw.get(name, {})
    if not isinstance(section, dict):
        warnings.append(f"[{name}] should be a table; ignored")
        return {}
    for key in section:
        if key not in _SECTIONS[name]:
            warnings.append(f"unknown key [{name}].{key} ignored")
    return section


def _text(
    section: dict[str, Any], key: str, default: str, warnings: list[str], where: str
) -> str:
    if key not in section:
        return default
    value = section[key]
    if not isinstance(value, str):
        warnings.append(f"[{where}] {key} should be a string; using {default!r}")
        return default
    return value.strip()


def _number(
    section: dict[str, Any], key: str, default: float, warnings: list[str], where: str
) -> float:
    if key not in section:
        return default
    value = section[key]
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        warnings.append(f"[{where}] {key} should be a number; using {default}")
        return default
    if value <= 0:
        warnings.append(f"[{where}] {key} must be positive; using {default}")
        return default
    return float(value)


def _whole(
    section: dict[str, Any], key: str, default: int, warnings: list[str], where: str
) -> int:
    return int(_number(section, key, float(default), warnings, where))


def _flag(
    section: dict[str, Any], key: str, default: bool, warnings: list[str], where: str
) -> bool:
    if key not in section:
        return default
    value = section[key]
    if not isinstance(value, bool):
        warnings.append(f"[{where}] {key} should be true or false; using {str(default).lower()}")
        return default
    return value


def _port(
    section: dict[str, Any], key: str, default: int, warnings: list[str], where: str
) -> int:
    """Like `_whole`, but 0 is meaningful: it asks the OS for a free port."""
    if key not in section:
        return default
    value = section[key]
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 65535:
        warnings.append(f"[{where}] {key} should be a port from 0 to 65535; using {default}")
        return default
    return value


def _read_provider(section: dict[str, Any], warnings: list[str]) -> str:
    value = _text(section, "provider", "gemini", warnings, "models").lower()
    if value not in PROVIDERS:
        raise ConfigError(
            f"[models] provider = {value!r} is not recognised. "
            f"Choose one of: {', '.join(PROVIDERS)}."
        )
    return value


def _read_models(section: dict[str, Any], provider: str, warnings: list[str]) -> dict[str, str]:
    allowed = choices_for(provider)
    fallback = default_model(provider)
    chosen: dict[str, str] = {}
    for role in ROLES:
        value = _text(section, role, fallback, warnings, "models")
        if value not in allowed:
            raise ConfigError(
                f"[models] {role} = {value!r} is not a model the {provider!r} provider will call.\n"
                f"Choose one of: {', '.join(known_models(provider))}, or {ADAPTIVE!r} to step "
                "down the ladder automatically."
            )
        chosen[role] = value
    return chosen


def _read_thinking(section: dict[str, Any], warnings: list[str]) -> dict[str, str]:
    levels: dict[str, str] = {}
    for role in ROLES:
        value = _text(section, role, DEFAULT_THINKING[role], warnings, "thinking").upper()
        if value not in THINKING_LEVELS:
            warnings.append(
                f"[thinking] {role} = {value!r} is not one of "
                f"{', '.join(THINKING_LEVELS)}; using {DEFAULT_THINKING[role]}"
            )
            value = DEFAULT_THINKING[role]
        levels[role] = value
    return levels


def _read_api_keys(section: dict[str, Any], warnings: list[str]) -> dict[str, str]:
    keys: dict[str, str] = {}
    for role in ("default",) + KEY_ROLES:
        value = _text(section, role, "", warnings, "api_keys")
        if value:
            keys[role] = value
    return keys


def _read_ladder(
    section: dict[str, Any], provider: str, warnings: list[str]
) -> tuple[str, ...]:
    allowed = known_models(provider)
    fallback = default_ladder(provider)
    value = section.get("ladder")
    if value is None:
        return fallback
    if not isinstance(value, Sequence) or isinstance(value, str):
        warnings.append("[adaptive] ladder should be a list of model IDs; using the default")
        return fallback

    ladder: list[str] = []
    for entry in value:
        if not isinstance(entry, str) or entry.strip() not in allowed:
            raise ConfigError(
                f"[adaptive] ladder contains {entry!r}, which is not a known {provider} model.\n"
                f"Use only: {', '.join(allowed)}."
            )
        model = entry.strip()
        if model not in ladder:
            ladder.append(model)
    if not ladder:
        warnings.append("[adaptive] ladder is empty; using the default")
        return fallback
    return tuple(ladder)


def _toml_string(text: str) -> str:
    if "\n" in text:
        body = text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"')
        return f'"""\n{body}\n"""'
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'
