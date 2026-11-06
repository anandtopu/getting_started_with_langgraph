# Verification notes

**Checked:** 2026-11-05, America/Chicago. **Status:** Phase 1 research plus Phase 2 foundation validation. The lockfile, shared helpers, gym, data generator, and introductory exercises now run locally. The full module course, live inference, and hosted deployment remain future work. See [the acceptance report](ACCEPTANCE_REPORT.md) for measured results.

## Versions and compatibility

The table records the current public PyPI version returned by each package's JSON API, its declared Python requirement, and the proposed course constraint. Sources link to the exact release, not a mutable latest-version page. Raw dependency declarations are retained in [pypi-metadata.json](verification/pypi-metadata.json); the MCP exception is recorded separately in [mcp-compatible.json](verification/mcp-compatible.json).

| Package | Latest stable observed | Declared Python requirement | Planned constraint / role | Source |
| --- | --- | --- | --- | --- |
| langgraph | 1.2.20 | >=3.10 | `>=1.2.20,<1.3` | [PyPI](https://pypi.org/project/langgraph/1.2.20/) |
| langchain-core | 1.7.6 | <4.0.0,>=3.10.0 | `>=1.7.6,<1.8` | [PyPI](https://pypi.org/project/langchain-core/1.7.6/) |
| langchain | 1.4.9 | <4.0.0,>=3.10.0 | `>=1.4.9,<1.5` | [PyPI](https://pypi.org/project/langchain/1.4.9/) |
| langgraph-checkpoint | 4.3.1 | >=3.10 | `>=4.3.1,<4.4` | [PyPI](https://pypi.org/project/langgraph-checkpoint/4.3.1/) |
| langgraph-checkpoint-sqlite | 3.1.3 | >=3.10 | `>=3.1.3,<3.2` | [PyPI](https://pypi.org/project/langgraph-checkpoint-sqlite/3.1.3/) |
| langgraph-checkpoint-postgres | 3.2.0 | >=3.10 | `>=3.2.0,<3.3` | [PyPI](https://pypi.org/project/langgraph-checkpoint-postgres/3.2.0/) |
| langgraph-prebuilt | 1.1.1 | >=3.10 | `Transitive: 1.1.1` | [PyPI](https://pypi.org/project/langgraph-prebuilt/1.1.1/) |
| langchain-openai | 1.7.4 | <4.0.0,>=3.10.0 | `>=1.7.4,<1.8` | [PyPI](https://pypi.org/project/langchain-openai/1.7.4/) |
| langchain-anthropic | 1.7.10 | <4.0.0,>=3.10.0 | `>=1.7.10,<1.8` | [PyPI](https://pypi.org/project/langchain-anthropic/1.7.10/) |
| langchain-google-genai | 4.4.3 | <4.0.0,>=3.10.0 | `>=4.4.3,<4.5` | [PyPI](https://pypi.org/project/langchain-google-genai/4.4.3/) |
| langchain-ollama | 1.1.0 | <4.0.0,>=3.10.0 | `>=1.1.0,<1.2` | [PyPI](https://pypi.org/project/langchain-ollama/1.1.0/) |
| langchain-mcp-adapters | 0.3.2 | >=3.10 | `>=0.3.2,<0.4` | [PyPI](https://pypi.org/project/langchain-mcp-adapters/0.3.2/) |
| mcp | 2.3.0 | >=3.10 | `>=1.30.0,<2` | [PyPI](https://pypi.org/project/mcp/2.3.0/) |
| langgraph-cli | 0.4.42 | >=3.10 | `>=0.4.42,<0.5 with inmem extra` | [PyPI](https://pypi.org/project/langgraph-cli/0.4.42/) |
| langgraph-sdk | 0.4.14 | >=3.10 | `>=0.4.14,<0.5` | [PyPI](https://pypi.org/project/langgraph-sdk/0.4.14/) |
| langgraph-api | 0.17.1 | >=3.11 | `Transitive: 0.17.1` | [PyPI](https://pypi.org/project/langgraph-api/0.17.1/) |
| langgraph-runtime-inmem | 0.37.1 | >=3.11.0 | `Transitive: 0.37.1` | [PyPI](https://pypi.org/project/langgraph-runtime-inmem/0.37.1/) |
| langsmith | 0.14.17 | >=3.10 | `>=0.14.17,<0.15` | [PyPI](https://pypi.org/project/langsmith/0.14.17/) |
| agentevals | 0.0.9 | >=3.9 | `>=0.0.9,<0.1` | [PyPI](https://pypi.org/project/agentevals/0.0.9/) |
| fastapi | 0.162.0 | >=3.10 | `>=0.162.0,<0.163` | [PyPI](https://pypi.org/project/fastapi/0.162.0/) |
| uvicorn | 0.54.0 | >=3.10 | `>=0.54.0,<0.55` | [PyPI](https://pypi.org/project/uvicorn/0.54.0/) |
| streamlit | 1.67.0 | >=3.11 | `>=1.67.0,<1.68` | [PyPI](https://pypi.org/project/streamlit/1.67.0/) |
| pytest | 9.2.0 | >=3.10 | `>=9.2.0,<9.3` | [PyPI](https://pypi.org/project/pytest/9.2.0/) |
| pytest-asyncio | 1.4.1.post1 | >=3.10 | `>=1.4.1.post1,<1.5` | [PyPI](https://pypi.org/project/pytest-asyncio/1.4.1.post1/) |
| pytest-socket | 0.8.1 | >=3.10 | `>=0.8.1,<0.9` | [PyPI](https://pypi.org/project/pytest-socket/0.8.1/) |
| hypothesis | 6.170.14 | >=3.11 | `>=6.170.14,<7` | [PyPI](https://pypi.org/project/hypothesis/6.170.14/) |
| ruff | 0.17.4 | >=3.7 | `>=0.17.4,<0.18` | [PyPI](https://pypi.org/project/ruff/0.17.4/) |
| pre-commit | 4.7.0 | >=3.11 | `>=4.7.0,<5` | [PyPI](https://pypi.org/project/pre-commit/4.7.0/) |
| nbstripout | 0.9.1 | >=3.10 | `>=0.9.1,<0.10` | [PyPI](https://pypi.org/project/nbstripout/0.9.1/) |
| jupyter | 1.1.1 | Not declared by the metapackage; inspect its dependencies | `>=1.1.1,<2` | [PyPI](https://pypi.org/project/jupyter/1.1.1/) |
| nbformat | 5.11.1 | >=3.10 | `>=5.11.1,<6` | [PyPI](https://pypi.org/project/nbformat/5.11.1/) |
| nbclient | 0.11.0 | >=3.10.0 | `>=0.11.0,<0.12` | [PyPI](https://pypi.org/project/nbclient/0.11.0/) |
| rich | 15.0.0 | >=3.9.0 | `>=15.0.0,<16` | [PyPI](https://pypi.org/project/rich/15.0.0/) |
| pydantic | 2.14.3 | >=3.10 | `>=2.14.3,<2.15` | [PyPI](https://pypi.org/project/pydantic/2.14.3/) |
| python-dotenv | 1.2.4 | >=3.10 | `>=1.2.4,<1.3` | [PyPI](https://pypi.org/project/python-dotenv/1.2.4/) |
| PyYAML | 6.0.3 | >=3.8 | `>=6.0.3,<7` | [PyPI](https://pypi.org/project/PyYAML/6.0.3/) |
| httpx | 0.28.1 | >=3.8 | `>=0.28.1,<0.29` | [PyPI](https://pypi.org/project/httpx/0.28.1/) |
| psycopg | 3.3.8 | >=3.10 | `>=3.3.8,<3.4 with binary,pool extras` | [PyPI](https://pypi.org/project/psycopg/3.3.8/) |
| reportlab | 5.1.0 | <4,>=3.9 | `>=5.1.0,<5.2` | [PyPI](https://pypi.org/project/reportlab/5.1.0/) |
| deepagents | 0.7.34 | <4.0,>=3.11 | `>=0.7.34,<0.8` | [PyPI](https://pypi.org/project/deepagents/0.7.34/) |
| uv | 0.13.7 | >=3.8 | `CLI recommendation: 0.13.7` | [PyPI](https://pypi.org/project/uv/0.13.7/) |
| hatchling | 1.33.0 | >=3.10 | `>=1.33.0,<1.34` | [PyPI](https://pypi.org/project/hatchling/1.33.0/) |
| fastmcp | 4.1.6 | >=3.10 | `Not in the core plan; Beta successor research only` | [PyPI](https://pypi.org/project/fastmcp/4.1.6/) |
| pycryptodome | 4.3.0 | >=3.9 | `>=4.3.0,<4.4` | [PyPI](https://pypi.org/project/pycryptodome/4.3.0/) |

The three core choices are mutually compatible at the metadata level: LangChain 1.4.9 requires LangGraph at least 1.2.12 and below 1.3, and core at least 1.7.5 and below 2. LangGraph 1.2.20 requires checkpoint 4.3 or newer and below 5; SQLite 3.1.3 requires checkpoint 4.3.1 or newer. The proposed ranges deliberately cap minor releases for the teaching surface. The lockfile will pin exact transitive versions; the ranges alone are not reproducibility.

**Resolver check completed:** the combined Python requirements, including provider integrations, apps, Postgres, the dev server, notebooks, evaluation, and deepagents, resolved successfully with `uv pip compile` in universal mode, with Python 3.11 as the lower target. [Input constraints](verification/requirements-plan.in) and [resolved versions](verification/resolved-plan.txt) are retained. This proves dependency metadata can be solved, not that every wheel or runtime works on every platform. The installed resolver was uv 0.12.18; the latest registry version observed was 0.13.7. The production `uv.lock`, clean-install checks, wheel availability, and Python/OS test matrix remain Phase 2 gates.

**Python target:** CPython 3.11–3.14; recommend 3.12. Streamlit, the dev-server runtime, and several developer tools require at least 3.11, although LangGraph alone supports 3.10. Use `requires-python = ">=3.11,<3.15"`; advertise the matrix as verified only after CI runs it.

### MCP exception

The requested standalone adapter 0.3.2 requires `mcp>=1.24,<2`; the latest official SDK is 2.3.0. The latest stable compatible SDK release observed is **1.30.0**, which the resolver selected. Keep the requested adapter + SDK 1.x route for module 16, with an explicit compatibility note. Do not claim SDK 2.3.0 works with this adapter. [Adapter metadata](https://pypi.org/pypi/langchain-mcp-adapters/0.3.2/json), [SDK 1.30.0](https://pypi.org/project/mcp/1.30.0/).

Current LangChain docs introduce `langchain.mcp.MCPAdapter`, built on FastMCP, as the successor. Its namespace is explicitly **Beta** and raises a Beta warning. Cover the direction and migration separately; do not silently mix its dependency set into the requested stable adapter examples. If the selected standalone release emits a deprecation warning in Phase 2, stop treating it as the warning-free main path: document the exact finding and select the documented successor as an explicitly Beta isolated module variant, with no blanket warning suppression. [MCP guide](https://docs.langchain.com/oss/python/langchain/mcp), [release notes](https://docs.langchain.com/oss/python/releases/changelog).

### Optional TypeScript stack

| Package/runtime | Verified registry version | Planned choice | Source |
| --- | --- | --- | --- |
| Node.js 24 LTS | 24.22.2, Krypton | Node 24 LTS for B1 | [Release index](https://nodejs.org/dist/index.json) |
| @langchain/langgraph | 1.7.1 | >=1.7.1,<1.8 | [npm](https://registry.npmjs.org/@langchain/langgraph/1.7.1) |
| @langchain/core | 1.3.5 | >=1.3.5,<1.4 | [npm](https://registry.npmjs.org/@langchain/core/1.3.5) |
| langchain | 1.6.2 | >=1.6.2,<1.7 | [npm](https://registry.npmjs.org/langchain/1.6.2) |
| typescript | 7.0.2 | >=7.0.2,<7.1 | [npm](https://registry.npmjs.org/typescript/7.0.2) |
| tsx | 4.23.15 | >=4.23.15,<4.24 | [npm](https://registry.npmjs.org/tsx/4.23.15) |
| zod | 4.6.7 | >=4.6.7,<4.7 | [npm](https://registry.npmjs.org/zod/4.6.7) |
| @types/node | 26.6.6 latest | 24.19.2 to match Node 24 | [compatible release](https://registry.npmjs.org/@types/node/24.19.2) |

See [npm metadata](verification/npm-metadata.json). Peer declarations for the LangChain packages align with these choices. An npm lockfile, clean install, and runtime parity tests have not been run; they are B1 implementation gates. TypeScript stream shapes are verified independently; Python's v2 envelope is not assumed to exist unchanged in JavaScript.

## Main invocation and streaming format

Use **explicit `version="v2"`** for Python Graph API `invoke`, `ainvoke`, `stream`, and `astream`. With the normal values-mode invoke, consume **`GraphOutput.value`** and **`GraphOutput.interrupts`**. The value follows the declared output schema, including Pydantic/dataclass coercion. Do not use deprecated dictionary-style access on GraphOutput. Non-values invoke modes return a list of stream parts, not the same GraphOutput contract. [Streaming guide](https://docs.langchain.com/oss/python/langgraph/streaming).

Stream consumers read the `type`, `ns`, and `data` fields. Values parts additionally carry interrupts. Teach updates and values first, then custom/debug, nested namespaces, message chunks, and finally checkpoints/tasks. Parallel events need not arrive in a fixed sibling order. The older default format is explained as something learners will encounter in existing examples; migration comparisons live in the migration guide. These choices keep one explicit envelope across the core course.

The current event-streaming guide recommends `stream_events`/`astream_events` with `version="v3"`, but the 1.2 release entry labels this API **Beta**, and the Deep Agents navigation still labels event streaming Beta. No explicit graduation entry was found in the checked changelog. Conservatively label the v3 extension **Beta**, explain the documentation discrepancy, and isolate it in module 18 and B4; do not misstate that it is absent or unrecommended. Its typed projections are a separate API from v2 stream-mode chunks. [Event streaming](https://docs.langchain.com/oss/python/langgraph/event-streaming), [Deep Agents overview](https://docs.langchain.com/oss/python/deepagents/overview).

## API and documentation decisions

| Area | Confirmed teaching direction | Official evidence | Implementation check still required |
| --- | --- | --- | --- |
| Graph construction and schemas | StateGraph, partial updates, separate schemas, reducer channels | [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api), [state](https://docs.langchain.com/oss/python/langgraph/graph-api-state) | Run every schema/output example against pinned packages |
| Conditional routing and Command | Data routing, updates plus goto, parent-directed handoffs | [Send and Command](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command) | Check all destination annotations and routes |
| Deferred nodes | `add_node` accepts `defer`; it waits for all pending tasks, not just immediate parents | [Control flow](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow) | Uneven and conditionally selected branch tests |
| Caching/retries/timeouts | add_node reference includes retry_policy, cache_policy, timeout, and error_handler | [API reference](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/add_node) | Pure cache key tests; transient/permanent failures; async-only timeouts |
| Recovery and draining | Runtime RunControl; checkpointed cooperative drain between supersteps | [Fault tolerance](https://docs.langchain.com/oss/python/langgraph/fault-tolerance) | Subprocess recovery and drain tests, no timing-dependent sleeps |
| Persistence | InMemorySaver, SqliteSaver, PostgresSaver; thread config and snapshot inspection | [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) | Context managers, setup, Windows connection cleanup |
| Human review | Dynamic interrupt/resume; node restarts on resume | [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) | Repeat effects, multiple IDs, rejection/edit validation |
| Context and tools | Runtime context and ToolRuntime; scoped Store/state; Command-returning tools | [Tools](https://docs.langchain.com/oss/python/langchain/tools) | Exact import paths and fake tool-call contracts |
| Prebuilt agents | create_agent and middleware | [Agents](https://docs.langchain.com/oss/python/langchain/agents), [migration guide](https://docs.langchain.com/oss/python/migrate/langgraph-v1) | No LangChain/LangGraph deprecation warnings |
| Multi-agent helpers | Teach direct tool/subgraph/handoff composition; no supervisor/swarm helper dependency | [Multi-agent](https://docs.langchain.com/oss/python/langchain/multi-agent), [supervisor migration](https://docs.langchain.com/oss/python/migrate/langgraph-supervisor) | Equivalence and context-isolation tests |
| Functional API | entrypoint/task, futures, saved task results; static visualization is limited | [Functional API](https://docs.langchain.com/oss/python/langgraph/functional-api) | Exact stream/output behavior and replay tests |
| Local evaluation | Deterministic trajectory matching; agentevals is available | [agentevals repository](https://github.com/langchain-ai/agentevals) | Exact matcher import and no-network tests |
| Local dev server | langgraph dev with CLI inmem extra; Studio/account requirements explicitly optional | [Local server](https://docs.langchain.com/oss/python/langgraph/local-server) | Export/import and startup checks; account-free local alternative |
| Deployment naming | Agent Server and LangSmith Deployment | [Deployment](https://docs.langchain.com/oss/python/langgraph/deploy) | Document actual access/licensing and test optional APIs separately |
| Checkpoint encryption | EncryptedSerializer with AES helper and externally supplied key | [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) | Key handling, round trip, deletion/retention limits |
| Deep agents | create_deep_agent; planning is explicitly configured; virtual filesystem and scoped subagents | [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) | Middleware defaults, backend constructors, fake-model compatibility |
| Recent features | Beta DeltaChannel, Beta v3 event projections, and per-call typed approval | [Changelog](https://docs.langchain.com/oss/python/releases/changelog) | Isolated examples and precise warning classifications |

The API reference was fetched directly as Markdown when the browser tool could not render it. The selected StateGraph.add_node parameters were inspected there. Forty distinct feature-map documentation URLs returned HTTP 200; the older memory URL redirects to the memory concepts page. [Reachability evidence](verification/source-checks.json). Reachability is not proof of every API signature or example; runnable contract checks remain mandatory before lesson code is accepted.

## Model settings

Only `.env.example` will contain default model identifiers; application code uses the model factory and configuration. `LLM_PROVIDER=ollama` selects the free local route; `LLM_MODEL` is an optional override. Provider-specific defaults stored in the environment template let a learner change just the provider line after supplying the relevant key and installing its optional integration. An explicit stale `LLM_MODEL` override is diagnosed rather than silently accepted for another provider.

| Provider | Documented candidate | Evidence and limits |
| --- | --- | --- |
| Ollama | qwen3:4b | [Ollama library](https://ollama.com/library/qwen3:4b) lists tool support and a 2.5 GB quantized download. Verified listing; local runtime/model has not been installed or called. |
| OpenAI | gpt-5.4-mini | [Official model page](https://developers.openai.com/api/docs/models/gpt-5.4-mini) lists function calling and structured output. No account-access or live call verified. |
| Anthropic | claude-haiku-5-5 | [Official model page](https://platform.claude.com/docs/en/models/haiku-5-5/overview) lists an active model and instructs callers to omit temperature/top-p/top-k. No live call verified. |
| Google Gemini | gemini-3.5-flash-lite | Phase 2 resolved the provisional capability check: the [official model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite?frmapp=yes) lists the stable identifier, function calling, and structured outputs. Its content was retrieved through search because direct browser retrieval redirects to AI Studio. No live call or account access verified. |

All graded comparisons use scripted fakes with temperature zero; temperature zero is not a promise that a real model is deterministic. Optional live models must use only supported parameters. In particular, do not pass temperature to the current Haiku candidate merely to match a generic helper signature. Hosted costs will be computed from documented token budgets and freshly checked pricing when each live walkthrough is written, not invented in this plan.

## Specification reconciliations

- Static breakpoints remain supported debugging features, not deprecated human-interaction APIs. Because the requested scanner forbids their spellings outside the migration guide, put their syntax and runnable debugging demonstration there; teach dynamic approval in core lessons. Do not inaccurately label every old alias as deprecated when it is only superseded.
- The first setup/install requires downloads. Offline means task and test execution after dependencies/data are installed; uncached `uv sync` cannot work without a package source.
- Tier 1 may use core message types for the required reducer introduction, but never imports provider integrations or makes model calls.
- The default install covers offline course tests; optional live/provider/server/app imports are lazy or tested through explicit extras. Run a separate all-extras suite before release; skipped optional tests are reported as skipped.
- Task bodies are incomplete only in the pedagogical sense: starters are executable, deliberately wrong implementations with `# YOUR CODE HERE`, never syntactic placeholders. Predict/Trace use answer files; Design separates mechanical acceptance from human rubric quality.
- Diagrams are generated from compiled graphs wherever the API supports them. Functional control-flow and system/deployment diagrams are explicitly labeled conceptual.
- No real payout, external email, or insurer system is contacted. The synthetic ledger uses integer cents and idempotency keys. Checkpointing alone does not make an external side effect exactly-once.

## Remaining verification gates

Before implementation is accepted: create the lockfile; run clean installs and the OS/Python matrix; inspect each used import and signature; execute all examples/notebooks; verify every code starter fails for its intended reason and every solution passes; validate the entire task and feature matrix; run lint/format, legacy-API and secret checks; perform local and external link checks; visually verify printable PDFs; and report real integration/live checks separately. No runtime or publication success is claimed by Phase 1.

## Phase 2 implementation evidence

The [package recheck](verification/phase_2_package_check.json) confirms the selected direct versions were still current and not yanked. The lock resolves 233 packages across supported environments. The base environment and all compatible Python extras installed successfully on Windows/Python 3.12.13; the all-extras environment contained 224 installed packages and passed the dependency consistency check.

The installed API probes confirm explicit v2 GraphOutput values, v2 stream-part fields, structured fake output, and the selected StateGraph node options. Tests additionally exercise ToolNode and create_agent with scripted tool calls, async model streaming, parallel reducer updates, checkpoints, and interrupt/resume. Category-specific LangGraph and LangChain deprecations are treated as errors.

All four live-provider constructors initialized with synthetic keys while an audit guard blocked connections. This checks adapter configuration, not service availability, model access, or generation. Hosted models receive no generic temperature override. The Ollama connectivity check is mocked only in this constructor probe; the ordinary --live diagnostic checks the configured service.

The all-extras suite passed 60 tests before the final progress-display and DNS-guard additions. The final base-suite result and exact checkpoint commands are in [the acceptance report](ACCEPTANCE_REPORT.md). The default environment was restored afterward. No API keys, live generation, hosted traces, Docker services, or remote CI were used.

For Windows async execution, the test harness permits only Python's internal socketpair construction; ordinary networking remains blocked. The gym additionally rejects DNS and connection audit events. Local checks needed normal Windows process/event-loop permissions in the authoring environment. This does not remove the test harness's network guards.

Representative estimate, receipt, and police-summary PDFs were rendered and inspected. All are readable single-page synthetic documents. Data tests check hashes, foreign keys, read-only access, two-run repeatability, cross-build logical SQLite rows, and hand-calculated money/routing boundaries.

CI uses [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1), [setup-uv v10.3.3](https://github.com/astral-sh/setup-uv), and uv 0.13.7. setup-uv's Python input sets UV_PYTHON, overriding the repository's 3.12 default so each matrix entry tests its declared interpreter. See the [official uv CI guidance](https://docs.astral.sh/uv/guides/integration/github/). Configuring these jobs is not evidence of a remote pass.
