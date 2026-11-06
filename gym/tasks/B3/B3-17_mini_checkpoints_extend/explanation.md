# Why the solution works

A checkpoint stores state and the next scheduled work for one thread. The mini runner copies snapshots so external mutation cannot corrupt history. Its single-node pause records a request and resumes the same pending node with a checked decision; another thread remains independent. This is a teaching representation, not LangGraph's full interrupt protocol.

Read the archived snapshot rather than an externally modified copy. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '"original_id": graph.latest("A").values["claim_id"]' to '"original_id": copy.values["claim_id"]'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
