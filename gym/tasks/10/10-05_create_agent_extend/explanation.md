# Why the solution works

create_agent builds a standard model/tool loop on LangGraph. Start there for ordinary tool use; use a custom StateGraph when the business process requires explicit gates or branches. The compiled agent still accepts state, can be inspected as a graph, and emits normal messages.

Pass through the requested policy instead of silently substituting another. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '"args": {"policy_id": policy_id}' to '"args": {"policy_id": "POL-0001"}'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
