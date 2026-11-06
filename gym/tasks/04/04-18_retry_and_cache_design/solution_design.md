# Worked design review

Retry a transient failure only when repeating the operation is safe. A cache stores a node result under a key; the key must include every input that changes that result. TTL expires a result after a duration, and an injected clock makes that behavior testable without sleeping.

- policy_read: choose retry_and_scoped_cache; this preserves the boundary exercised by the example.
- payout_write: choose idempotency_before_retry; this preserves the boundary exercised by the example.
- ttl_test: choose injected_clock; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
