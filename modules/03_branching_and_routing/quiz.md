# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_conditional_router.py using one claim from its input cases.
2. Diagnose this broken behavior: Path-map values must match each intended destination. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_command_routes.py using one claim from its input cases.
4. Diagnose this broken behavior: A competing static edge schedules an extra acknowledgment. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_early_exit.py using one claim from its input cases.
6. Diagnose this broken behavior: Zero is a defined boundary, not an omitted case. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A routing function chooses a label from current state. A path map connects that label to a real node. A total router has an outcome for every accepted input, including zero, missing evidence, unknown categories, and malformed amounts.
2. Path-map values must match each intended destination. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Command combines state updates with a routing instruction. Its destination annotation helps describe possible edges. A static edge still runs even when a Command chooses another node, so use one routing mechanism at a decision point.
4. A competing static edge schedules an extra acknowledgment. Compare the normal case with the boundary fixtures and identify the first differing update.
5. Termination is a routing outcome, not an exceptional Python crash. Screen invalid and duplicate claims before assigning work. The returned state should still explain why a claim ended so an adjuster can inspect it.
6. Zero is a defined boundary, not an omitted case. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
