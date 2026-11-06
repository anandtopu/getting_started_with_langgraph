# Why the solution works

Resuming a Functional API interrupt restarts the entrypoint from its beginning. Completed task results are retrieved from checkpoints, so the task body need not run again. Keep task ordering deterministic and validate the resume payload. External effects still require their own idempotency at the crash window.

Use a task boundary so completed evidence can be reused during replay. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '@task\n    def collect_evidence' to 'def collect_evidence'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
