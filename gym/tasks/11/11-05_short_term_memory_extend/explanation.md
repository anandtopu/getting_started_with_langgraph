# Why the solution works

Checkpoint history and model context are different collections. Trimming chooses a bounded view for one call without deleting the saved conversation. A summarization node retains a short factual digest; in this small example it joins customer statements deterministically. Production summaries need factual evaluation and a token counter appropriate to the model.

Include newly supplied evidence in the summary. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes '" | ".join(facts[-2:])' to '" | ".join(facts[:1])'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
