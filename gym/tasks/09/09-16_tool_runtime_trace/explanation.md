# Why the solution works

ToolRuntime injects trusted context, graph state, the Store, and tool_call_id without exposing them as model-selectable fields. A tool returning Command can update graph state and acknowledge its own request. Customer identity belongs in authenticated context, not in an argument the model invents.

Keep the graph state consistent with the Store write. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '"saved_preference": preference' to '"saved_preference": "phone"'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
