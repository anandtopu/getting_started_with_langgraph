# Why the solution works

Stateless workers share durable checkpoints, ownership records, and effect keys. One active run may mutate a thread at a time. The local registry demonstrates lease exclusion within one process; the Postgres implementation uses a transaction-scoped advisory lock across workers. A new ledger instance proves that idempotency survives worker replacement, and conflicting payloads are rejected.

Exercise and reject idempotency-key reuse with a changed payload. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '+ int(case["changed_payload"])' to '+ 0'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
