# Why the solution works

The TypeScript model factory returns a scripted LangChain fake with tool calls. A manual StateGraph loop and createAgent consume the same trajectory, making their roles and call identities directly comparable. The Python gym bridge executes the selected TypeScript file in Node; it never supplies the business answer itself.

Preserve the expected tool-call identity across the language port. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'id: "lookup-1"' to 'id: "wrong-call"'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
