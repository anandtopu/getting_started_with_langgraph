# Why the solution works

A channel is one state field together with its update rule. The default rule overwrites. An Annotated reducer combines the old and new values. Associativity means grouping updates differently does not change the result, which matters when branches complete in batches.

Severity must not decrease when a later finding is weaker. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'max(indexed.get(key, {}).get("severity", 0), finding["severity"])' to 'finding["severity"]'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
