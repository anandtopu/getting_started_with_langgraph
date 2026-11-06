# Course acceptance report

Measured locally on November 6, 2026, on Windows/Python 3.12.13. The complete implementation is present; the public cross-platform and Docker acceptance run is the remaining release gate. This report will be updated with the actual workflow result.

## Delivered

- 23 core modules and four bonuses, each with three examples, a use case, a notebook, a quiz, and graded practice.
- 486 tasks across 81 feature groups; 414 core and 72 bonus tasks.
- Five runnable capstones with independently specified acceptance cases, selectable learner-file grading, evaluation sets, generated diagrams, extensions, and rubrics.
- Twelve cumulative Claims Copilot versions; authenticated FastAPI streaming, a Streamlit dashboard, local SQLite persistence, and Docker/Postgres deployment.
- Synthetic claims, customers, policies, documents, emails, and evaluation fixtures; no real customer data.
- Linked coverage, learning schedules, 30 observed bugs, 88 glossary terms, troubleshooting, migration notes, and five printable one-page PDFs.

## Local evidence

| Check | Result |
| --- | --- |
| Clean base install and tests | 307 passed, 64 explicitly skipped optional checks |
| Full regression suite | 377 tests passed; the one link-check failure was repaired and all five content tests then passed |
| Capstone reference acceptance | 18 passed |
| Gym release validation | All 486 tasks checked; one TypeScript starter fault was repaired and its complete task validation passed on rerun |
| Updated Beta stream exercise | Tool arguments reconstructed from two actual deltas; changed task validation passed |
| Examples and cumulative use cases | 110 passed offline, none skipped |
| Notebooks | All 27 executed in real kernels; committed outputs cleared |
| Ruff lint and format | Passed, more than 3,200 Python files checked |
| TypeScript | Strict type checking passed; Node executed all three implementations through the Python grading bridge |
| Coverage and prohibited API scan | Zero problems |
| Local and external links | 2,841 checked, zero problems |
| Printable PDFs | Five PDFs, one page each, rendered and visually inspected |
| Dependency metadata | 44 Python packages rechecked; compatible pinned family retained |

Reproduce the full checks with the commands in [optional dependencies](OPTIONAL_DEPENDENCIES.md), [README](../README.md), and [the workflow](../.github/workflows/ci.yml). The release gym command refuses missing optional dependencies. Default tests report optional skips explicitly.

## Integration boundaries

The local machine's selected Docker context has no running engine, so container and actual Postgres acceptance are delegated to the public workflow. That workflow starts the real services, pauses a claim, restarts the API, resumes approval, verifies one synthetic payment effect, tests cross-worker leases, and reopens durable customer memory. Configuration alone is not a passing deployment test.

No live model inference, hosted tracing, managed deployment, real payment, or email was performed. Provider constructor probes use synthetic credentials and blocked networking. Beta warnings are expected only for explicitly marked B4 APIs; LangGraph and LangChain deprecations remain test errors. The application uses fixed synthetic identities; production authentication and provider billing accounting require additional integration.

A cached fresh-clone foundation quick start previously completed in 14.57 seconds. That measures command execution, not a beginner's learning time or an uncached download. A final fresh-clone smoke check and public CI results remain to be recorded.
