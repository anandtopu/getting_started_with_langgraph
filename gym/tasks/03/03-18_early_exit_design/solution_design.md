# Worked design review

Termination is a routing outcome, not an exceptional Python crash. Screen invalid and duplicate claims before assigning work. The returned state should still explain why a claim ended so an adjuster can inspect it.

- negative: choose invalid; this preserves the boundary exercised by the example.
- duplicate: choose end_before_assignment; this preserves the boundary exercised by the example.
- zero: choose eligible; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
