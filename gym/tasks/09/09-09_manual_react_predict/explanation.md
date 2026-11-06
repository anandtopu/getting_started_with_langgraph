# Why the solution works

A manual agent loop alternates a model node and ToolNode. tools_condition checks the newest AI message: tool calls continue the loop, a final answer ends it. A recursion budget catches nontermination, but does not authorize tool effects or guarantee a useful answer.

Return tool evidence to the model before ending. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'graph.add_edge("tools", "call_model")' to 'graph.add_edge("tools", END)'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
