# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_short_term_memory.py using one claim from its input cases.
2. Diagnose this broken behavior: Use a new message ID for a new turn instead of overwriting the previous turn. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_store_namespaces.py using one claim from its input cases.
4. Diagnose this broken behavior: Delete the actual memory key. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_semantic_and_privacy.py using one claim from its input cases.
6. Diagnose this broken behavior: Delete checkpoint history separately from Store records. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. Checkpoint history and model context are different collections. Trimming chooses a bounded view for one call without deleting the saved conversation. A summarization node retains a short factual digest; in this small example it joins customer statements deterministically. Production summaries need factual evaluation and a token counter appropriate to the model.
2. Use a new message ID for a new turn instead of overwriting the previous turn. Compare the normal case with the boundary fixtures and identify the first differing update.
3. The Store holds cross-thread memories under tuple namespaces. Semantic memory stores facts, episodic memory stores events, and procedural memory stores instructions; these are application conventions rather than special database types. Customer-scoped namespaces must be enforced from trusted context. Deleting a memory is an explicit operation.
4. Delete the actual memory key. Compare the normal case with the boundary fixtures and identify the first differing update.
5. An embedding maps text into numbers so the Store can rank similarity within a namespace. These transparent word vectors make the offline ranking reproducible. Store deletion does not delete old checkpoint contents: retention must handle both systems separately. Retrieval is evidence selection, never an authorization check.
6. Delete checkpoint history separately from Store records. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
