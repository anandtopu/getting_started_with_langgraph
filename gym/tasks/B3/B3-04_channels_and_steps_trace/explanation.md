# Why the solution works

The educational runner snapshots state before a superstep, collects writes from every sibling, then applies them at a barrier. Thus both workers see zero prior findings while the next-step summary sees both. This small runner explains visibility; it deliberately omits production concurrency, async execution, pending-write recovery, and serialization.

Report the previous-boundary view seen by each worker. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'len(state["findings"])' to 'len(state["findings"]) + 1'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
