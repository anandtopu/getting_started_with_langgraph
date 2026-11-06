# Why the solution works

An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.

Labels need case normalization before comparison. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'value.strip().lower()' to 'value.strip()'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
