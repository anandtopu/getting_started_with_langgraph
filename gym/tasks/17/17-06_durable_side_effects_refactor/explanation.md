# Why the solution works

A task result is reusable only after it is checkpointed. This example kills an owned child after the effect ledger commits but before the task returns, then starts a new process. A payload-bound idempotency key prevents duplicate effects even in that gap. sync, async, and exit durability offer different checkpoint guarantees; none makes an external system transactional with the graph.

Report the durable ledger count, not an inferred execution count. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '"effect_count": len(result["effects"])' to '"effect_count": len(result["effects"]) + 1'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
