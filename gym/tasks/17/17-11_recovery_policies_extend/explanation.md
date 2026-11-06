# Why the solution works

RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.

Honor the cooperative shutdown request at the next boundary. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'if case["drain"]:' to 'if False:'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
