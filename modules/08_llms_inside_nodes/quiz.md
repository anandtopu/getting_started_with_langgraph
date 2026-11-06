# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_model_boundary.py using one claim from its input cases.
2. Diagnose this broken behavior: Include exactly 100000 cents in fast-track routing. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_message_identity.py using one claim from its input cases.
4. Diagnose this broken behavior: Correct an existing message without appending another customer message. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_tokens_and_fakes.py using one claim from its input cases.
6. Diagnose this broken behavior: Read the documented node name from stream metadata. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A model predicts text from messages; a prompt is its instruction and evidence. Structured output parses that text into a validated schema. Validation can reject an impossible amount, but cannot prove a claim is true. The deterministic router owns the decision after extraction.
2. Include exactly 100000 cents in fast-track routing. Compare the normal case with the boundary fixtures and identify the first differing update.
3. MessagesState applies add_messages: a matching message ID replaces a message instead of appending a duplicate. RemoveMessage deletes by that same ID. Tool responses still need the tool_call_id from their AI request; message identity and tool-call identity serve different purposes.
4. Correct an existing message without appending another customer message. Compare the normal case with the boundary fixtures and identify the first differing update.
5. The messages stream emits a chunk and metadata inside each v2 part's data field. Assemble content in order and inspect langgraph_node to attribute it. A fake should agree between invoke and stream, including a structured JSON response; it tests orchestration, not model quality.
6. Read the documented node name from stream metadata. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
