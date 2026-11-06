# Why the solution works

A trajectory is the sequence of tool requests, separate from the final answer. agentevals can compare strict order, unordered calls, subsets, or supersets. Exact argument matching catches the right tool used on the wrong policy. Choose the matching rule from the business requirement; parallel independent calls may legitimately change order.

Check the policy arguments, not only tool names. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'tool_args_match_mode="exact"' to 'tool_args_match_mode="ignore"'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
