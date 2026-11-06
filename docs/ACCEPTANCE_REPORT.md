# Course acceptance report

All seven implementation phases are complete. The [repository review](reviews/2026-11-06/README.md) fixed 23 runtime, grading, and teaching issues. Its [final acceptance workflow](https://github.com/anandtopu/getting_started_with_langgraph/actions/runs/42259016717) passed **all 14 jobs** on November 6, 2026 for [88332b0](https://github.com/anandtopu/getting_started_with_langgraph/commit/88332b09198cae903bfade24920d1ebd2c246082). The [current validation evidence](reviews/2026-11-06/ACTION_PLAN.md) records 410 passing tests and the investigation of one earlier, unreproduced Windows grading mismatch.

The historical measurements below come from the [original build acceptance workflow](https://github.com/anandtopu/getting_started_with_langgraph/actions/runs/42185228068) for [eabf7f6](https://github.com/anandtopu/getting_started_with_langgraph/commit/eabf7f6ad146c9e7e787cc6e5457f20340eaeed1).

## Delivered

- 23 core modules and four bonuses, each with three examples, a use case, a notebook, a quiz, a graph diagram, and graded practice.
- 486 tasks across 81 feature groups: 414 core and 72 bonus exercises.
- Five runnable capstones with independent acceptance cases, selected-file grading, evaluation sets, generated diagrams, extensions, and self-review rubrics.
- Twelve cumulative Claims Copilot versions; authenticated FastAPI streaming, a Streamlit dashboard, SQLite persistence, and Docker/Postgres deployment.
- Reproducible synthetic claims, customers, policies, documents, emails, and evaluation fixtures.
- Linked learning schedules and coverage, 30 observed bugs, 88 glossary terms, troubleshooting and migration guides, and five printable single-page PDFs.

## Original build results

| Check | Observed result |
| --- | --- |
| Core platform matrix | Windows and Linux: Python 3.11, 3.12, 3.13, 3.14; macOS: Python 3.12; all nine jobs passed |
| Complete-course matrix | Python 3.12 on Windows, Linux, and macOS; all three jobs passed |
| Full local regression suite | 378 passed; two explicitly Beta streaming warnings |
| Clean base Python environment | 307 passed and 64 optional skips locally with Node dependencies already present; clean CI also skips the TypeScript bonus until npm dependencies are installed |
| Gym release checks | All 486 references, deliberate starter failures, standalone code runs, written-answer oracles, and hint packages passed |
| Capstones | 18 reference acceptance cases passed; all five selected-file validators confirmed reference passes, intended starter failures, and standalone execution |
| Examples and cumulative use cases | All 110 executed offline, none skipped in the complete environment |
| Notebooks | All 27 executed in real kernels on all three complete-course platforms; committed outputs remain cleared |
| Python and TypeScript quality | Ruff lint and format checks passed; strict TypeScript checking passed |
| Coverage, links, prohibited APIs | Release coverage, local/external links, and legacy API checks passed |
| Docker/Postgres | Real services passed health checks, durable pause/restart/resume, customer-role rejection, stale approval rejection, one synthetic payment effect, cross-worker leases, payload-bound idempotency, and Store reopen checks |
| Dashboard controls | Local Streamlit AppTest passed open claim, attach estimate, confirm coverage, approve, and display final status using synthetic HTTP responses |
| Printable guides | Five PDFs, one page each, rendered and visually inspected; regenerated fixture PDF also rechecked |
| Fresh public clone | Clone, new environment, first graph, intentionally failing starter, repair, passing check, and progress report completed in 21.57 seconds with existing download caches and credentials removed |

The [machine-readable CI evidence](verification/final_ci.json) records every job and step. Reproduce the checks using [the workflow](../.github/workflows/ci.yml), [optional dependency instructions](OPTIONAL_DEPENDENCIES.md), and [README](../README.md). Full release validation refuses missing optional dependencies; base tests report explicit skips.

## Definition of done

- [x] A base installation passes tests without API keys or execution-time external networking.
- [x] Ruff lint and formatting pass.
- [x] Linux and Windows CI pass on every supported Python version, with additional macOS coverage.
- [x] The gym exceeds 140 tasks: all 486 validate, with 18 tasks and at least five task types per module, progressive hints, and complete explanations.
- [x] All gym commands are exercised by the CLI tests on Windows, macOS, and Linux.
- [x] Tier 1 runs without a live model or provider integration.
- [x] The prohibited-API scanner has a negative test; LangGraph and LangChain deprecations remain test errors. Explicit Beta warnings are allowed in B4.
- [x] Every module includes the required lesson sections, three examples, a use case, quiz, tests, notebook, and prediction exercise.
- [x] Feature-map and common-bug links resolve; local and external link checks pass.
- [x] Automated clone-to-first-pass is under ten minutes. The measured 21.57 seconds used cached downloads; novice learning time and an uncached download were not measured.
- [x] Executable files are complete and checked. Starters are intentionally faulty programs, not missing implementations. Design rationale quality requires the supplied human self-review rubric.

## Portability fixes verified during acceptance

Windows/Python 3.14 exposed different compressed PDF bytes for identical content. Small fixture PDFs now use invariant metadata and uncompressed streams; generation and integrity tests pass across the matrix. A macOS run exposed a parallel Trace exercise with duplicate sort keys. Its displayed records now sort by both role and evidence, preserving the intentional business fault while making the answer deterministic.

## Optional checks and limits

No live model inference, hosted tracing, managed-service deployment, real payment, or external email was performed. Provider constructor probes use synthetic credentials with networking blocked. Python 3.14 reports an upstream LangSmith asyncio deprecation warning; it is visible and distinct from the prohibited LangGraph/LangChain APIs. The application uses synthetic fixed identities and a demonstration ledger; production identity integration and provider billing accounting remain application-specific work described in [deployment](DEPLOYMENT.md).
