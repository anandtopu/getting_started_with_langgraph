# Why the solution works

Memory persistence ends with its process. A SQLite saver stores checkpoints on disk and must remain open for every invocation that uses it. Explicit context managers release connections, including on Windows where open files can prevent cleanup.

Resource-lifetime refactoring must preserve continuation input. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '"estimate attached"' to '"received"'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
