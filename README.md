# Crude Agentic Mathematical Research System

A prototype agentic research assistant for hard mathematical problems. It is
**not** a theorem prover. Given a problem, it explores approaches, proposes
proof attacks, hunts for obstacles and counterexamples, searches the
literature, and keeps a persistent research graph of everything it has
considered — deciding continuously what to look at next.

A planner acts as research director. Six specialized worker roles operate as
independent sources of ideas: **Searcher** (literature retrieval), **Toy Example**
(concrete constructions), **Counterexample** (falsification attempts),
**Decomposer** (subgoal planning), **Sketcher** (proof sketches and calculations),
and **Verifier** (claim validation). The graph is research memory, not a fact
database. An asyncio event loop lets the director react the moment any single
worker or literature call finishes, instead of running fixed rounds. Each role
has its own model, thinking level and API key.

## Install

```powershell
python -m pip install -r math_agent/requirements.txt
```

Then open `math_agent/run_config.toml`, put a key under `[api_keys]`, and check
the connection. `smoke_test` calls every role the configured mode will use, so a
bad key or an unavailable model shows up before a real run:

```powershell
python -m math_agent.smoke_test
```

## Configure

Everything about a run lives in `math_agent/run_config.toml`; the command line
takes no arguments. `run_config.example.toml` is the documented template, and
the live file is gitignored so an inline key never lands in a repo.

| Table | What it sets |
| --- | --- |
| `[run]` | `mode`, the problem (inline or `problem_file`), `tag`, `resume` |
| `[budget]` | The three caps plus `max_concurrent_workers` |
| `[models]` | One model per role, or `adaptive`. Roles: `planner`, `explorer`, `mathematician`, `skeptic`, `verifier`, `baseline` |
| `[thinking]` | `LOW` / `MEDIUM` / `HIGH` reasoning depth per role |
| `[api_keys]` | A key per role, or a shared `default` |
| `[adaptive]` | The fallback ladder and its cooldown |
| `[literature]` | OpenAlex contact address, results per search |
| `[viewer]` | The live graph view: on/off, port, browser, poll interval |

`mode` selects the entry point: `main` for the full system, or `baseline_a`,
`baseline_b`, `baselines_both` for the comparison arms.

### Worker roles

The six specialized workers replace the old Explorer/Mathematician/Skeptic triad:

| Role | Function | Bills API key pool |
| --- | --- | --- |
| `searcher` | Literature retrieval, known theorems with hypotheses, search queries | `explorer` |
| `toy_example` | Construct small/degenerate examples, verify assumptions hold | `explorer` |
| `counterexample` | Falsify claims by constructing counter-instances | `skeptic` |
| `decomposer` | Propose multiple subgoal decomposition plans | `mathematician` |
| `sketcher` | Proof sketches and simple calculations for subgoals | `mathematician` |
| `verifier` | Check claimed proofs/lemmas step-by-step; verdict HOLDS/GAP/FALSE | `explorer` |

### Models

Each of `planner`, `explorer`, `mathematician`, `skeptic`, `verifier` and `baseline` takes
one of:

| Value | Notes |
| --- | --- |
| `gemini-3.7-flash` | Strongest, most often contended |
| `gemini-3.6-flash` | |
| `gemini-3.5-flash` | |
| `gemini-3.5-flash-lite` | Cheapest, highest availability |
| `adaptive` | Walk the `[adaptive] ladder`, best model first |

The six worker slots map onto three API key pools: `explorer` (searcher, toy_example, verifier), `mathematician` (decomposer, sketcher), and `skeptic` (counterexample).

An `adaptive` role tries the strongest model on the ladder. When one answers 429
or 503 it is demoted for `cooldown_seconds` and the call steps down immediately
rather than sitting in backoff; once the cooldown lapses that model returns to
the front and gets probed again, so a run recovers instead of finishing on the
weakest model. Every switch is logged, and `summary.md` reports which models
actually served the calls.

### API keys

A role uses its own key, else `[api_keys].default`, else the `GEMINI_API_KEY`
environment variable. Giving each role its own key keeps one project's quota
from throttling the whole run. Keys are never printed or written into a run
directory; the banner shows only a fingerprint such as `set (...1a2b)`.

The six worker slots share three API key pools:
- `explorer` pool: searcher, toy_example, verifier
- `mathematician` pool: decomposer, sketcher  
- `skeptic` pool: counterexample

## Run

From the directory that contains `math_agent/`:

```powershell
cd C:\Users\samfe\OneDrive\Desktop
python -m math_agent
```

Or double-click-equivalent: `powershell -File math_agent\run.ps1`.

Press Ctrl-C at any time; the graph and event log are flushed on the way out.

The older module entry points still work and take flags that override the config
file for one run:

```powershell
python -m math_agent.main "a different problem"
python -m math_agent.main --file problem.txt --max-planner-calls 15 --max-worker-calls 12
python -m math_agent.main --resume math_agent/runs/20260821-213000
python -m math_agent.baselines "your problem here" --arm A
```

## Watching the graph grow

A run serves a live view of its own research graph at `http://127.0.0.1:8765/`
and opens it for you. Nodes appear as the planner records them, statuses change
colour as claims are promoted or killed off, and the activity panel shows what
each worker is doing.

The viewer is a read-only observer of the `graph.json` and `events.jsonl` the run
already writes, so it cannot influence or slow the research. It is plain HTML and
hand-written JavaScript with no external requests, and it listens on the loopback
interface only.

| Encoding | Meaning |
| --- | --- |
| Green | `PROMISING` |
| Amber | `OBSTACLE` |
| Blue | `IDEA` |
| Grey | `UNVERIFIED`, and dimmed for `DEAD_END` |
| Purple | `POTENTIALLY_RELEVANT`, so papers |
| Red | `REJECTED` |
| Ringed centre node | The problem itself |
| Dashed edge | `contradicts` or `blocks` |
| White pulse | Just arrived, or just changed status |
| Node size | Number of connections |

Click a node to read it in full, with its status history, notes and links. Drag a
node to pin it, scroll to zoom, drag the background to pan, and click a status in
the legend to fade it out. The view keeps reframing itself as the graph grows
until you move the camera yourself; `Fit` hands it back.

To watch a run from a separate window, or to reopen a finished one:

```powershell
python -m math_agent.viewer                                    # newest run
python -m math_agent.viewer --run math_agent/runs/20260821-221418
python -m math_agent.viewer --port 9000 --no-open
python -m math_agent.viewer --run math_agent/runs/20260821-221418 --export # standalone HTML
```

Set `[viewer] enabled = false` if you would rather a run kept its console to
itself. The baseline arms have no graph, so they have no viewer.

## Recreating the Graph & Compiling Results

Every successful run automatically generates both a standalone interactive HTML graph and a compiled Markdown dossier in its run directory. You can also recreate the graph or re-compile results for any past run on demand:

```powershell
# Recreate interactive graph AND compile all results for the newest run:
python -m math_agent.report --all

# For a specific past run:
python -m math_agent.report --run math_agent/runs/20260821-222552 --all

# Recreate just the standalone interactive graph (opens in your default browser):
python -m math_agent.report --run math_agent/runs/20260821-222552 --graph

# Recreate using the local HTTP viewer server:
python -m math_agent.report --run math_agent/runs/20260821-222552 --graph --serve

# Compile all findings into a single Markdown dossier with LLM report instructions:
python -m math_agent.report --run math_agent/runs/20260821-222552 --compile
```

### Standalone Interactive Graph (`interactive_graph.html`)
The exported HTML graph embeds all nodes, edges, activity feed, and styling in a single, self-contained file. It runs locally in any modern browser without needing Python or an active web server—making it ideal for offline review, presentations, or sharing.

### Compiled Results & LLM Report Prompt (`compiled_results.md`)
Aggregates all exploration artifacts into a single dossier:
- Run metadata, timing, models, and token consumption
- Director's synthesis from `summary.md`
- Complete research graph inventory organized by status
- Full, unabridged worker derivations and formulas from all six specialized workers (Searcher, Toy Example, Counterexample, Decomposer, Sketcher, Verifier)
- Retrieved literature and paper searches
- Preceded by a rigorous system prompt instructing any frontier LLM (e.g., Gemini 1.5 Pro, Claude 3.5 Sonnet, GPT-4o) to synthesize the raw experimental findings into a formal, publication-grade mathematical research report.

## Output

Each run writes `math_agent/runs/<timestamp>/`:

| File | Contents |
| --- | --- |
| `interactive_graph.html` | Self-contained interactive graph (offline, zero-server) |
| `compiled_results.md` | Complete dossier of all findings + LLM report prompt |
| `graph.json` | The research graph, rewritten after every mutation |
| `events.jsonl` | Every event, one JSON object per line |
| `log.txt` | The timestamped console transcript |
| `summary.md` | Final report: promising ideas, obstacles, dead ends, papers |
| `config_used.toml` | The settings this run resolved to, with keys redacted |

## Baselines

The point of the architecture is to beat a single model call. Arms A and B run
on the same problem, and should be given the same models as arm C so that any
difference is architectural:

- `mode = "baseline_a"` — one Gemini call
- `mode = "baseline_b"` — 3 workers in parallel (searcher, sketcher, counterexample), no graph, no event loop
- `mode = "baselines_both"` — both arms in one run
- `mode = "main"` — arm C, the full system with six specialized workers

Then rate arm A, arm B and arm C on novelty, usefulness, diversity of
approaches, obstacles identified, literature found, and whether the system found
anything the baseline missed.

## How it works

```
event arrives -> planner sees event + relevant graph slice -> planner returns
structured actions -> Python executes them -> new events -> planner reacts
```

The planner never manipulates Python objects directly. It returns actions
(`ADD_NODE`, `UPDATE_NODE`, `ADD_EDGE`, `ASSIGN_TASK`, `CANCEL_TASK`,
`SEARCH_PAPERS`, `GET_PAPER`, `FINISH`) which are executed deterministically.

Workers run as background `asyncio` tasks, so the supervisor handles whichever
result arrives first and can change strategy before the others finish.

Nothing a worker says is treated as true. Every claim node carries a status:
`IDEA`, `PROMISING`, `UNVERIFIED`, `OBSTACLE`, `DEAD_END`, `REJECTED`,
`POTENTIALLY_RELEVANT`, and a `created_by` field for provenance indicating which
specialized worker (searcher, toy_example, counterexample, decomposer, sketcher,
verifier) generated it.

## Cost control

`[budget]` caps every run on three axes: `max_planner_calls`,
`max_worker_calls`, and `max_wall_clock_seconds`. Whichever trips first ends
the run cleanly and writes the summary. Token usage is printed at the end.

## Literature tools

OpenAlex (primary), Semantic Scholar and arXiv, all free and keyless. Set
`[literature] openalex_mailto` to your email to use OpenAlex's polite pool (the
`OPENALEX_MAILTO` environment variable still wins if set). Open-access
PDFs are fetched and text-extracted with `pypdf`; otherwise the abstract is
used. Retrieved papers always enter the graph as `POTENTIALLY_RELEVANT`.

## Layout

```
math_agent/
  run_config.toml    the one file you edit before a run
  __main__.py        python -m math_agent: runs whatever the config says
  main.py            the full system, plus override flags
  run_config.py      config loading and validation
  models.py          model choice and the adaptive fallback ladder
  config.py          the settings surface the rest of the package reads
  gemini_client.py   shared async Gemini wrapper, one client per API key
  viewer/            live graph view: local server plus a single HTML page
  baselines.py       comparison arms A and B
  agent/             planner, action schema, prompts (six worker role prompts)
  workers/           six specialized roles: searcher, toy_example, counterexample, decomposer, sketcher, verifier
  graph/             research graph + JSON persistence
  tools/             openalex, semantic_scholar, arxiv, papers
  events/            event bus and supervisor loop
```
