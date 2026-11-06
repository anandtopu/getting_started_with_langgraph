# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_intake_nodes.py using one claim from its input cases.
2. Diagnose this broken behavior: A graph node must return a mapping of state updates. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_wire_pipeline.py using one claim from its input cases.
4. Diagnose this broken behavior: Validation must occur before acknowledging the claim. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_draw_and_explain.py using one claim from its input cases.
6. Diagnose this broken behavior: The intended final node must be connected. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. State is the information available to a graph. TypedDict documents its keys. A node is a function that reads state and returns only the keys it changes; the graph merges those updates instead of replacing the whole state.
2. A graph node must return a mapping of state updates. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Edges declare which node can run next. START is the entry point and END marks termination. compile checks the graph and creates an executable object. Explicit v2 invoke returns GraphOutput; its value is the final state.
4. Validation must occur before acknowledging the claim. Compare the normal case with the boundary fixtures and identify the first differing update.
5. A generated diagram shows the compiled edges rather than a hand-drawn guess. In a sequential graph each node runs in a later superstep, a batch of work that sees the previous batch's committed updates. Updates reveal which node actually ran.
6. The intended final node must be connected. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
