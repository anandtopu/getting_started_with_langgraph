# Why the solution works

ainvoke awaits one result; astream yields intermediate parts. Pass RunnableConfig into async model calls for explicit context propagation. The seven v2 modes expose different views, so count types rather than assuming one common payload. Cancellation must await cleanup; a browser disconnect is not proof that an external effect was rolled back.

Record cleanup after the waiting node receives cancellation. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'cleaned.append("closed")' to 'cleaned.clear()'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
