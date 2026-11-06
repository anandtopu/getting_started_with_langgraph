# Worked design review

The dashboard is a projection of server events: append progress and text, replace pending approvals when a new snapshot arrives. Streamlit session state remembers the selected thread between UI reruns. Client-side controls improve usability, while the API independently rejects stale or unauthorized decisions. Beta v3 typed projections are explored in B4; this UI uses stable v2-derived SSE.

- state: choose session_projection; this preserves the boundary exercised by the example.
- pending: choose replace_on_snapshot; this preserves the boundary exercised by the example.
- authority: choose server_recheck; this preserves the boundary exercised by the example.

Rejected alternative: combine all decisions in an unvalidated, mutable global state. It hides ownership and makes independent failure checks harder. Validate normal, boundary, and rejected cases; retain the original synthetic input for comparison. This reference earns full marks only when those checks and the written rationale are both present.
