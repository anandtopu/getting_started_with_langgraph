# Why the solution works

A pytest test is a function whose assertions express requirements. Parametrized tests run it over many inputs. Compare pure node rules and whole graphs against independently specified boundary outcomes; comparing two copies of the same implementation can preserve the same bug. Fake models make orchestration tests repeatable, not model accuracy measurable.

Require both implementations to match the independent expected route. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'row["expected"] == row["rule"] == row["graph"]' to 'row["expected"] != row["rule"] == row["graph"]'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
