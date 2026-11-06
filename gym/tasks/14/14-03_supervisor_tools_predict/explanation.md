# Why the solution works

A supervisor may call specialists as tools. Each specialist gets a narrow evidence prompt and a private message history; the supervisor receives only the returned conclusion. This direct create_agent pattern avoids an extra helper package. More agents add calls and failure boundaries, so compare them against a single-agent baseline.

Register both specialist capabilities with the supervisor. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'tools=[policy_expert, fraud_analyst]' to 'tools=[policy_expert]'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
