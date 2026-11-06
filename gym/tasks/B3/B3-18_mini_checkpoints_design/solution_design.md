# Worked design review

A checkpoint stores state and the next scheduled work for one thread. The mini runner copies snapshots so external mutation cannot corrupt history. Its single-node pause records a request and resumes the same pending node with a checked decision; another thread remains independent. This is a teaching representation, not LangGraph's full interrupt protocol.

- checkpoint: choose copied_state_and_position; this preserves the boundary exercised by the example.
- thread: choose isolated; this preserves the boundary exercised by the example.
- pause: choose single_node_teaching_contract; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
