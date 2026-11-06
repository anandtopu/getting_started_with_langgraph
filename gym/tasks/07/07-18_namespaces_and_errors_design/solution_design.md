# Worked design review

A subgraph namespace identifies nested work. Sibling parallel events can arrive in either order; causal requirements, such as summary after both checks, are stable. A live event trace is not itself the durable checkpoint history.

- siblings: choose unordered_within_superstep; this preserves the boundary exercised by the example.
- summary: choose after_both_checks; this preserves the boundary exercised by the example.
- history: choose checkpoints_not_events; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
