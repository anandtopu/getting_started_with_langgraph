# Review action plan

## Release gate

All confirmed findings R01–R23 have fixes. The [final acceptance workflow](https://github.com/anandtopu/getting_started_with_langgraph/actions/runs/42259016717) passed all 14 jobs on November 6, 2026 for [88332b0](https://github.com/anandtopu/getting_started_with_langgraph/commit/88332b09198cae903bfade24920d1ebd2c246082). The earlier unexplained Windows observation remains documented below.

## Fix queue

| IDs | Priority | Owner | Action | Acceptance |
| --- | --- | --- | --- | --- |
| R01–R07 | P1/P2 | Runtime maintainer | Correct resume, identity, intake, and UI boundaries | Independent API, workflow, identity, and Streamlit regressions |
| R08–R09, R18, R22–R23 | P2/P3 | Gym maintainer | Reject incomplete grading, invalidate stale evidence, support external TypeScript workspaces, and preserve worker failures | Negative grader/CLI/progress, external-workspace, and worker-exit tests |
| R10, R19–R21 | P2/P3 | Runtime maintainer | Correct budget, lease/key, and SSE edge behavior | Boundary tests and persistence acceptance |
| R11–R14 | P2 | Course maintainer | Repair task semantics and introductory/live teaching | All 486 task packages; examples; notebook execution |
| R15–R17 | P2 | Course maintainer | Demonstrate replay, align deployment input, preserve generation | Capstone acceptance, graph-input regression, regeneration/quality checks |

## Validation results

| Check | Measured result |
| --- | --- |
| Full pytest suite | 410 passed, 1 optional live test skipped in complete-course CI; two expected Beta streaming warnings |
| Practice Gym | All 486 packages pass on Windows, Linux, and macOS, including reference behavior, intended starter failures, structural requirements, extension compatibility, and written-answer checks |
| Capstones | All five references pass, starters fail for their intended acceptance reason, standalone runs succeed on all three complete-course platforms |
| Examples/use cases | 111 executed offline, no optional skips on all three complete-course platforms |
| Notebooks | All 27 executed in real kernels on Windows, Linux, and macOS; committed outputs remain cleared |
| Trace evidence | All 80 generated traces recaptured and compared with grading answers; 61 contain in-process node callbacks, with pauses, handoffs, cancellation, and failures distinguished |
| Real SQLite API | Owned loopback server stopped and restarted; saved interrupt survives, role and stale-decision checks pass, exactly one synthetic effect |
| Docker/Postgres | Real services pass restart/resume, role restrictions, stale-decision rejection, one synthetic effect, cross-worker leases, payload-bound idempotency, and Store reopen checks |
| Code/docs | Ruff lint/format, strict TypeScript, release coverage, prohibited-API scan, and local/public links pass |

[Machine-readable CI evidence](../../verification/review_ci.json) records every job and step. The matrix covers Python 3.11–3.14 on Windows/Linux and Python 3.12 on macOS, plus all-extra course runs on all three platforms. The closing commit updates documentation and verification records only.

## Follow-up backlog

### Intermittent validation result

[Run 42254285399](https://github.com/anandtopu/getting_started_with_langgraph/actions/runs/42254285399) observed one Windows oracle mismatch in task 17-03. The old log omitted the observed answer, so its underlying cause was not established. The task's saved grading answer remains unchanged. Eighty parallel oracle repetitions (320 crash/restart cases) and twelve deliberately delayed checkpoint-write probes passed locally. Worker failures now preserve their error exit and details, and future oracle mismatches print the actual result. The final CI run passed every exercise on all three platforms, including Windows task 17-03. The earlier incident remains an unconfirmed intermittent reliability risk rather than a claimed root-cause fix.

### Optional empirical checks

These are empirical limits, not unresolved confirmed bugs: exercise a real configured provider when explicitly desired; measure novice learning time; obtain learner feedback on repeated batch/input-boundary practice; perform account-specific managed deployment when requested. The repository's fixed-identity demo is not a substitute for production identity integration or live provider accounting.
