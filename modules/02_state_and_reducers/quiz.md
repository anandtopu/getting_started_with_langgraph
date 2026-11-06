# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_schema_contracts.py using one claim from its input cases.
2. Diagnose this broken behavior: Use Pydantic field access or model_dump instead of losing validated values. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_reducer_findings.py using one claim from its input cases.
4. Diagnose this broken behavior: Return new evidence only; the reducer already has previous values. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_state_boundaries.py using one claim from its input cases.
6. Diagnose this broken behavior: Use the same message ID to replace the original message. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. TypedDict describes a dictionary for type checking; it does not validate values at runtime. Dataclasses give attribute access and defaults. Pydantic checks fields at the boundary. With explicit v2 output, preserve the schema's object type before extracting its fields.
2. Use Pydantic field access or model_dump instead of losing validated values. Compare the normal case with the boundary fixtures and identify the first differing update.
3. A channel is one state field together with its update rule. The default rule overwrites. An Annotated reducer combines the old and new values. Associativity means grouping updates differently does not change the result, which matters when branches complete in batches.
4. Return new evidence only; the reducer already has previous values. Compare the normal case with the boundary fixtures and identify the first differing update.
5. Input and output schemas define an API boundary; private channels can still exist inside the graph. Messages are records with roles, text, and IDs. add_messages appends new IDs and replaces an existing ID, so correcting one message need not duplicate it.
6. Use the same message ID to replace the original message. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
