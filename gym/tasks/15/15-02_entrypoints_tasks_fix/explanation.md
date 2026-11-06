# Why the solution works

An entrypoint accepts one serializable input and uses ordinary Python branches. A task call schedules durable work and returns a future; result() obtains its value. This supports familiar control flow without removing the need for validated inputs and deterministic replay order.

Match the Graph API fast-track boundary. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'claim["amount_cents"] <= 100000' to 'claim["amount_cents"] < 100000'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
