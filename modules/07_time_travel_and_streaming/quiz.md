# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_replay_and_fork.py using one claim from its input cases.
2. Diagnose this broken behavior: Replay the new fork configuration, not its uncorrected parent. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_v2_stream_parts.py using one claim from its input cases.
4. Diagnose this broken behavior: The state payload is inside data, not at the envelope root. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_namespaces_and_errors.py using one claim from its input cases.
6. Diagnose this broken behavior: Keep parent and child scopes distinct. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A checkpoint configuration identifies a historical state. Replaying it reruns later work; it does not merely print an old answer. update_state with as_node forks from that checkpoint and schedules its successors. Approval encountered again is requested again.
2. Replay the new fork configuration, not its uncorrected parent. Compare the normal case with the boundary fixtures and identify the first differing update.
3. A v2 stream part has type, ns, and data fields. Updates contain a node's changed fields; values contain the visible whole state; custom events carry application progress. Interrupt metadata is separate from ordinary values and must survive UI serialization.
4. The state payload is inside data, not at the envelope root. Compare the normal case with the boundary fixtures and identify the first differing update.
5. A subgraph namespace identifies nested work. Sibling parallel events can arrive in either order; causal requirements, such as summary after both checks, are stable. A live event trace is not itself the durable checkpoint history.
6. Keep parent and child scopes distinct. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
