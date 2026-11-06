# Worked design review

A generated diagram shows the compiled edges rather than a hand-drawn guess. In a sequential graph each node runs in a later superstep, a batch of work that sees the previous batch's committed updates. Updates reveal which node actually ran.

- visibility: choose previous_superstep; this preserves the boundary exercised by the example.
- diagram: choose generated_from_compiled_graph; this preserves the boundary exercised by the example.
- termination: choose acknowledge_to_end; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
