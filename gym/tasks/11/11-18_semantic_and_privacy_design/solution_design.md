# Worked design review

An embedding maps text into numbers so the Store can rank similarity within a namespace. These transparent word vectors make the offline ranking reproducible. Store deletion does not delete old checkpoint contents: retention must handle both systems separately. Retrieval is evidence selection, never an authorization check.

- retrieval: choose namespace_then_similarity; this preserves the boundary exercised by the example.
- retention: choose store_and_checkpoints; this preserves the boundary exercised by the example.
- embeddings: choose deterministic_teaching_vectors; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
