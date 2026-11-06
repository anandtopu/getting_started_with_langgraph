# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_shared_subgraph.py using one claim from its input cases.
2. Diagnose this broken behavior: Apply the high-value risk boundary inside the reusable child. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_schema_adapters.py using one claim from its input cases.
4. Diagnose this broken behavior: Preserve the exact review threshold. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_subgraph_persistence.py using one claim from its input cases.
6. Diagnose this broken behavior: Reject a string masquerading as a human decision. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A compiled subgraph can be a parent node when their state keys agree. Its updates still meet the parent's reducers. This fraud checker is reused for claims and new policies; its idempotent flag reducer avoids duplicating shared evidence when the child returns accumulated state.
2. Apply the high-value risk boundary inside the reusable child. Compare the normal case with the boundary fixtures and identify the first differing update.
3. When parent and child schemas differ, call the child inside an adapter node. Map the input fields explicitly, then return only the public finding. Private child fields should not become parent state just because a dictionary is convenient to copy.
4. Preserve the exact review threshold. Compare the normal case with the boundary fixtures and identify the first differing update.
5. A parent checkpointer propagates into its child. A child compiled with the default per-invocation behavior starts fresh for each invocation; checkpointer=True gives the child persistent state across calls. While paused, get_state(subgraphs=True) exposes the nested task snapshot. Streaming namespaces identify which graph emitted an update.
6. Reject a string masquerading as a human decision. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
