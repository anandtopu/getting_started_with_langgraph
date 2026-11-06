# Why the solution works

interrupt pauses graph work and returns a request to the caller. A checkpointer and stable thread preserve that pause. Command(resume=...) supplies the response; the interrupted node restarts, so validate the response rather than trusting its shape.

Validate adjuster identity from the trusted invocation configuration, independently of the response payload. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'the new node or boundary contract described above' to 'the deliberately incomplete extension'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
