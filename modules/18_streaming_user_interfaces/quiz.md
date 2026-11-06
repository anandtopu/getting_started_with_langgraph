# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_async_streams.py using one claim from its input cases.
2. Diagnose this broken behavior: Request the intended seven stream projections. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_sse_api.py using one claim from its input cases.
4. Diagnose this broken behavior: Carry a rejection through the authenticated workflow. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_adjuster_dashboard.py using one claim from its input cases.
6. Diagnose this broken behavior: Replace the stale approval identity with the current snapshot. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. ainvoke awaits one result; astream yields intermediate parts. Pass RunnableConfig into async model calls for explicit context propagation. The seven v2 modes expose different views, so count types rather than assuming one common payload. Cancellation must await cleanup; a browser disconnect is not proof that an external effect was rolled back.
2. Request the intended seven stream projections. Compare the normal case with the boundary fixtures and identify the first differing update.
3. An SSE frame ends with a blank line and carries JSON on its data line. JSON escaping keeps embedded newlines inside one frame. The real FastAPI routes authenticate callers, check thread ownership, and bind resumed decisions to the current interrupt ID. Reconnect by reading a snapshot; this demo does not promise durable replay from Last-Event-ID.
4. Carry a rejection through the authenticated workflow. Compare the normal case with the boundary fixtures and identify the first differing update.
5. The dashboard is a projection of server events: append progress and text, replace pending approvals when a new snapshot arrives. Streamlit session state remembers the selected thread between UI reruns. Client-side controls improve usability, while the API independently rejects stale or unauthorized decisions. Beta v3 typed projections are explored in B4; this UI uses stable v2-derived SSE.
6. Replace the stale approval identity with the current snapshot. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
