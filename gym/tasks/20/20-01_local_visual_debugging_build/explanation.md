# Why the solution works

langgraph.json maps a public graph name to a Python export. The local Agent Server hosts that graph; Studio adds a visual client and may require an account. Without Studio, draw_mermaid, updates, and checkpoint snapshots still reveal the route and pause. The export leaves persistence to the server instead of constructing its own competing saver.

Resolve the graph name declared in the server configuration. The implementation preserves the claim identity and separates the tested concern from unrelated state. The cases include normal and boundary inputs, so replacing the result with a single constant is not a general repair.

The deliberate fault changes 'config["graphs"]["claims"]' to 'config["graphs"]["missing"]'. Follow the data affected by that operation before inspecting later nodes. For predictions, distinguish returned values from error types. For traces, the observed failure is evidence of the first broken contract, not proof that the framework is unreliable.

Run the task tests against your selected workspace file. Viewing this reference is assisted study; a written Design rationale still requires the rubric.
