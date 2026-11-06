# Why the solution works

Beta v3 event streaming exposes typed message, subgraph, value, and output projections. Child messages belong to the subgraph projection. The raw protocol uses method and params rather than the v2 type/ns/data shape. This example uses a fresh fake run for raw-event inspection so consuming one view does not pretend to replay already-consumed events.

Consume the raw protocol when inspecting lifecycle channels. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'events = list(raw)' to 'events = []'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
