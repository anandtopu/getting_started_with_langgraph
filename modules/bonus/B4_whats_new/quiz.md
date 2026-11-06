# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_event_streaming_beta.py using one claim from its input cases.
2. Diagnose this broken behavior: Read the final model message from the completed output projection. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_delta_channels_beta.py using one claim from its input cases.
4. Diagnose this broken behavior: Honor and validate the requested snapshot cadence. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_typed_approvals.py using one claim from its input cases.
6. Diagnose this broken behavior: Respect rejection instead of coercing every decision to approval. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. Beta v3 event streaming exposes typed message, subgraph, value, and output projections. Child messages belong to the subgraph projection. The raw protocol uses method and params rather than the v2 type/ns/data shape. This example uses a fresh fake run for raw-event inspection so consuming one view does not pretend to replay already-consumed events.
2. Read the final model message from the completed output projection. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Beta DeltaChannel stores incremental writes and reconstructs channel state through a deterministic batch reducer. snapshot_frequency bounds how often a full snapshot is written. The reducer must be invariant to regrouping write batches, because replay may batch differently from live execution. Schema and reducer changes require migration testing before reusing old threads.
4. Honor and validate the requested snapshot cadence. Compare the normal case with the boundary fixtures and identify the first differing update.
5. Per-call HumanInTheLoopMiddleware emits one approval request for each gated tool call. Its response_schema describes only permitted decisions; the runtime validates the answer before saving it. Resume by interrupt ID and keep tool editing disabled when the reviewer may approve or reject only. Typed approval validates shape, while real authorization still belongs to the application.
6. Respect rejection instead of coercing every decision to approval. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
