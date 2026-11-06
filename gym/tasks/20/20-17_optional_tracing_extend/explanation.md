# Why the solution works

LangSmith tracing is optional and independent of checkpoint persistence. A local trace can show an old route, locate the checkpoint before routing, fork with corrected data, and retain the original history. This example explicitly disables remote tracing. Enable hosted tracing only for sanitized data and an account you intend to use.

Keep the original route distinct from the corrected branch. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '"original_route": history[0].values["route"]' to '"original_route": result.value["route"]'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
