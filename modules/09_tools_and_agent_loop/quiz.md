# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_tools_and_messages.py using one claim from its input cases.
2. Diagnose this broken behavior: Return a correlated tool error for an unknown policy. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_manual_react.py using one claim from its input cases.
4. Diagnose this broken behavior: Let the agent observe a policy lookup failure. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_tool_runtime.py using one claim from its input cases.
6. Diagnose this broken behavior: Keep the graph state consistent with the Store write. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A tool's typed parameters become a schema the model can request. ToolNode runs the requested function and returns a ToolMessage with the original call ID. Expected lookup failures become error messages when error handling is enabled. A payout calculator proposes cents; it does not transfer money.
2. Return a correlated tool error for an unknown policy. Compare the normal case with the boundary fixtures and identify the first differing update.
3. A manual agent loop alternates a model node and ToolNode. tools_condition checks the newest AI message: tool calls continue the loop, a final answer ends it. A recursion budget catches nontermination, but does not authorize tool effects or guarantee a useful answer.
4. Let the agent observe a policy lookup failure. Compare the normal case with the boundary fixtures and identify the first differing update.
5. ToolRuntime injects trusted context, graph state, the Store, and tool_call_id without exposing them as model-selectable fields. A tool returning Command can update graph state and acknowledge its own request. Customer identity belongs in authenticated context, not in an argument the model invents.
6. Keep the graph state consistent with the Store write. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
