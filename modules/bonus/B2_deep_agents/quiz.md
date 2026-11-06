# Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_deep_agent_planning.py using one claim from its input cases.
2. Diagnose this broken behavior: Keep task progress consistent with the supplied status. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_virtual_filesystem.py using one claim from its input cases.
4. Diagnose this broken behavior: Deny writes outside the permitted virtual directory. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_deep_subagents.py using one claim from its input cases.
6. Diagnose this broken behavior: Preserve a human rejection of delegation. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. This pinned release uses explicit TodoListMiddleware for planning. The write_todos tool updates declared task state; marking an item completed is not evidence that the underlying investigation actually happened.
2. Keep task progress consistent with the supplied status. Compare the normal case with the boundary fixtures and identify the first differing update.
3. StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.
4. Deny writes outside the permitted virtual directory. Compare the normal case with the boundary fixtures and identify the first differing update.
5. A deep-agent specialist has an explicit name, scoped tools, and isolated context. Delegation itself is gated by human approval and the parent has a model-call budget. The specialist receives a narrow policy question rather than the whole customer file. A rejected delegation must not execute the specialist task.
6. Preserve a human rejection of delegation. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>
