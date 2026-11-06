# Why the solution works

Command combines state updates with a routing instruction. Its destination annotation helps describe possible edges. A static edge still runs even when a Command chooses another node, so use one routing mechanism at a decision point.

A competing static edge schedules an extra acknowledgment. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'graph.add_edge(START, "triage")' to 'graph.add_edge(START, "triage")\n    graph.add_edge("triage", "acknowledge")'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
