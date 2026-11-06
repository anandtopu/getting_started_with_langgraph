# Why the solution works

On resume, Python starts the interrupted node again. Code before interrupt can therefore repeat. Move effects after validated approval into separate checkpointed work, and use a stable idempotency key because a crash can occur after a write but before its checkpoint.

Effects before interrupt repeat when the node restarts. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'entries.append("review")' to 'entries.append("review")\n        notifications[str(len(entries))] = "Premature notification"'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
