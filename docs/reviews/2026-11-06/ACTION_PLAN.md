# Review action plan

## Release gate

All confirmed findings R01–R22 have fixes. Completion requires the final full tests, exercise/capstone validation, notebooks, quality checks, and platform CI. This file is updated with measured results after those checks finish.

## Fix queue

| IDs | Priority | Owner | Action | Acceptance |
| --- | --- | --- | --- | --- |
| R01–R07 | P1/P2 | Runtime maintainer | Correct resume, identity, intake, and UI boundaries | Independent API, workflow, identity, and Streamlit regressions |
| R08–R09, R18 | P2/P3 | Gym maintainer | Reject incomplete grading and invalidate stale evidence | Negative grader/CLI/progress tests |
| R10, R19–R21 | P2/P3 | Runtime maintainer | Correct budget, lease/key, and SSE edge behavior | Boundary tests and persistence acceptance |
| R11–R14 | P2 | Course maintainer | Repair task semantics and introductory/live teaching | All 486 task packages; examples; notebook execution |
| R15–R17 | P2 | Course maintainer | Demonstrate replay, align deployment input, preserve generation | Capstone acceptance, graph-input regression, regeneration/quality checks |

## Validation results

| Check | Measured local result |
| --- | --- |
| Full pytest suite | 401 passed, 1 optional live test skipped; subsequent redaction, external-workspace, and compatibility regressions also passed targeted checks |
| Practice Gym | All 486 packages exercised; the expanded baseline sweep found three incompatible extensions, then all three passed targeted validators after correction |
| Capstones | All five references pass, starters fail for their intended acceptance reason, standalone runs succeed |
| Examples/use cases | 111 executed offline, no optional skips |
| Notebooks | All 27 executed in real kernels; committed outputs remain cleared |
| Real SQLite API | Owned loopback server stopped and restarted; saved interrupt survives, role and stale-decision checks pass, exactly one synthetic effect |
| Code/docs | Ruff lint/format, strict TypeScript, release coverage, prohibited-API scan, and 3,062 local/public links pass |

Cross-platform CI is the final release gate and is recorded after the pushed implementation finishes.

## Follow-up backlog

These are empirical limits, not unresolved confirmed bugs: exercise a real configured provider when explicitly desired; measure novice learning time; obtain learner feedback on repeated batch/input-boundary practice; perform account-specific managed deployment when requested. The repository's fixed-identity demo is not a substitute for production identity integration or live provider accounting.
