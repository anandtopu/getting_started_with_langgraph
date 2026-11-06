# Why the solution works

An adapter node converts a business question into private agent messages and returns only the public explanation. The parent retains claim identity and its own process status. Sharing every internal message is convenient but widens the context and privacy boundary unnecessarily.

Map the specialist answer into the parent explanation field. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'return {"explanation": result.value["messages"][-1].content}' to 'return {}'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
