# Worked design review

An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.

- acceptance: choose known_and_unknown_labels; this preserves the boundary exercised by the example.
- whitespace: choose strip_then_lower; this preserves the boundary exercised by the example.
- evidence: choose passing_assertions; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
