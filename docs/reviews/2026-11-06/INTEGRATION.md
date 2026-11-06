# Cross-file integration review

## Scope

The second pass traced authenticated UI requests through ownership, graph checkpoints, resume validation, synthetic effects, and public projections; authoring sources through generated tasks, graders, progress, and documentation; and deployment configuration through graph exports and durable storage.

## Findings and resolution

| Flow | Cross-file problem | Resolution / acceptance |
| --- | --- | --- |
| HTTP decision → checkpoint → retry | Node validation happened after the resume value was saved. A normal correction request could reuse the bad saved value. | Validate before Command, then check the current interrupt again under the lease. Invalid receipt followed by valid receipt completes without a payment. |
| Identity → model/tool work → Store | Namespacing alone did not establish trusted ownership. | Authorize before Copilot work; take QA identity from Runtime context. The application already maps fixed demo tokens to server-owned principals. |
| Fixture → extraction → fraud review → public result | Missing fixture amounts passed early intake examples but broke later composed versions. | Defer extraction/policy arithmetic for rejected intake and guard risk arithmetic. Original evidence is preserved, with no fabricated amount. |
| UI widget → selected claim → cached SSE text | Changing a widget default changed its identity, while the display cache lacked an identity boundary. | Stable key and explicit thread handoff; clear cache on endpoint/token/thread changes. |
| Starter → tests → progress | A behavioral mutation was mislabeled Refactor, skipped checks could count as a pass, and changed tests did not invalidate progress. | Preserve behavioral baselines, add structural checks, reject skipped acceptance, and fingerprint grading contracts. |
| Example → extension → old tests | Existing features were removed and described as additions. | Separate new-capability tests from compatibility checks; batch additions preserve the original entry point exactly. |
| Saved history → replay claim | Reading an already-complete checkpoint was described as replay. | Execute from a historical pending node and prove work happened; human decisions are requested again where appropriate. |
| Agent Server plan → exported graph | The planner and graph expected different input shapes. | Generate a real claim-state payload and invoke it in an independent test. |
| Canonical sources → published lessons | Ad hoc diagram/link changes disappeared during regeneration. | Repeatable builders, retained Fix links, checked-in generated overviews, and documented regeneration order. |

## Checks retained

Fixed demo identities remain explicitly scoped. Payment authorization is enforced independently of model output. SQLite is a single-process teaching backend; Postgres uses a transaction-scoped advisory lock for cross-worker exclusion and payload-bound effect idempotency. The Compose stack binds the published ports to loopback, requires configured secrets, waits for database health, and runs as a non-root user. Dependency versions remain locked; this review does not perform an unrelated upgrade.

The early letter says review is complete and no payment has been issued; the final public summary supplies the separate payment status. This was inspected and was not treated as a false payment authorization.

## Limits

No real provider inference or managed deployment is necessary for offline acceptance. The added provider lab is opt-in and its deterministic results do not establish live-model quality. The local grader runs trusted learner code on the learner's machine; network blocking and environment filtering do not turn it into a hostile-code isolation service. Written Design quality and novice comprehension require human review.
