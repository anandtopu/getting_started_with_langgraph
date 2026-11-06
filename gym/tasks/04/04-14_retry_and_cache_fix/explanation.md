# Why the solution works

Retry a transient failure only when repeating the operation is safe. A cache stores a node result under a key; the key must include every input that changes that result. TTL expires a result after a duration, and an injected clock makes that behavior testable without sleeping.

Customer identity belongs in the cache key. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '[state["customer_id"], state["policy_version"], state["amount_cents"]]' to '[state["policy_version"], state["amount_cents"]]'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
