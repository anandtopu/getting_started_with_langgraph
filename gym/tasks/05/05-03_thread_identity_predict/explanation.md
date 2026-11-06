# Why the solution works

A checkpointer saves graph state under a thread ID. New input on that thread starts another run against its saved state. Resuming a pending operation is different: use the saved continuation or an interrupt response rather than pretending it is a new claim.

Saved notes must survive a second invocation on the same graph. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'checkpointer=InMemorySaver()' to 'checkpointer=None'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
