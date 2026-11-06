# Worked design review

Parallel pauses can be answered with an interrupt-ID-to-response map. IDs identify requests; list order does not. Validate each edited value against its own schema and business limit before merging it into state.

- response_address: choose interrupt_id; this preserves the boundary exercised by the example.
- amount: choose bounded_integer_cents; this preserves the boundary exercised by the example.
- date: choose iso_date_validation; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
