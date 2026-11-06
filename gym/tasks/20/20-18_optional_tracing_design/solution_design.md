# Worked design review

LangSmith tracing is optional and independent of checkpoint persistence. A local trace can show an old route, locate the checkpoint before routing, fork with corrected data, and retain the original history. This example explicitly disables remote tracing. Enable hosted tracing only for sanitized data and an account you intend to use.

- tracing: choose optional; this preserves the boundary exercised by the example.
- evidence: choose local_checkpoints; this preserves the boundary exercised by the example.
- correction: choose retained_branch; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
