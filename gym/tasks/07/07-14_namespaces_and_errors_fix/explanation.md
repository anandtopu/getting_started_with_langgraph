# Why the solution works

A subgraph namespace identifies nested work. Sibling parallel events can arrive in either order; causal requirements, such as summary after both checks, are stable. A live event trace is not itself the durable checkpoint history.

Keep parent and child scopes distinct. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'if not part["ns"]' to 'if part["ns"]'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
