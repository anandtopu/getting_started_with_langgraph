# Why the solution works

The self-hosted stack has an API, Postgres, and a Streamlit UI. Database readiness gates API startup, and API health gates the UI. Required credentials come from the environment; published ports bind to localhost for this teaching deployment. The example validates the committed configuration, while the integration job actually starts the containers and calls the service.

Detect accidental public binding of the teaching service. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'not binding.startswith("127.0.0.1:")' to 'False'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
