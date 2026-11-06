# Worked design review

A trajectory is the sequence of tool requests, separate from the final answer. agentevals can compare strict order, unordered calls, subsets, or supersets. Exact argument matching catches the right tool used on the wrong policy. Choose the matching rule from the business requirement; parallel independent calls may legitimately change order.

- trajectory: choose tool_requests; this preserves the boundary exercised by the example.
- order: choose business_contract; this preserves the boundary exercised by the example.
- arguments: choose exact; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
