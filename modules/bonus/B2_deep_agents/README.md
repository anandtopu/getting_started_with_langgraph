# B2 — Deep agents on LangGraph

> After this module you can plan a larger claim investigation using explicit planning and bounded subagents.

**Time:** 180 minutes · **Level:** Advanced · **LLM needed:** No live model · **Cost:** $0 with the included fakes.

**Larkspur Claims Copilot v11** · Practice takes additional time.

## Prerequisites

Complete [LangGraph.js](../B1_langgraph_js/README.md). Read dictionary keys, functions, and Python type hints comfortably. Run uv sync from the repository root.

Optional installation requirements are listed in [the setup guide](../../../docs/OPTIONAL_DEPENDENCIES.md). Use `uv run --no-sync` after installing extras so subsequent commands retain that environment.

## Learning objectives

- Implement and explain create_deep_agent; explicit TodoListMiddleware; planning tools; task progress; current defaults.
- Implement and explain Virtual filesystem; StateBackend; file tools; bounded paths; persisted artifacts; no host-shell tools.
- Implement and explain Subagent definitions; private context; bounded delegation; explicit tools; checkpoints and approval.

## The big idea

Plan a larger claim investigation using explicit planning and bounded subagents. Predict the state before running code, then compare the observed result. A state is the data visible to a node; a node is one unit of work; an edge selects later work. A checkpoint is a saved state boundary, not a promise that an external effect happened exactly once.

## How it works

### Deep Agent Planning

create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. This pinned release uses explicit TodoListMiddleware for planning. The write_todos tool updates declared task state; marking an item completed is not evidence that the underlying investigation actually happened.

A visible investigation checklist helps organize work, but checked boxes still need supporting records.

### Virtual Filesystem

StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.

A virtual filing tray is part of the case record, not unrestricted access to the building's cabinets.

### Deep Subagents

A deep-agent specialist has an explicit name, scoped tools, and isolated context. Delegation itself is gated by human approval and the parent has a model-call budget. The specialist receives a narrow policy question rather than the whole customer file. A rejected delegation must not execute the specialist task.

The lead adjuster needs approval to commission a specialist and sends only the relevant question.

## Key APIs at a glance

| API / executable example | What it does | When to use it |
| --- | --- | --- |
| AIMessage, HumanMessage, TodoListMiddleware — [01_deep_agent_planning.py](examples/01_deep_agent_planning.py) | create_deep_agent; explicit TodoListMiddleware; planning tools; task progress; current defaults | create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. |
| AIMessage, HumanMessage, InMemorySaver — [02_virtual_filesystem.py](examples/02_virtual_filesystem.py) | Virtual filesystem; StateBackend; file tools; bounded paths; persisted artifacts; no host-shell tools | StateBackend stores a virtual filesystem in graph state instead of writing host files. |
| AIMessage, HumanMessage, InMemorySaver, Command — [03_deep_subagents.py](examples/03_deep_subagents.py) | Subagent definitions; private context; bounded delegation; explicit tools; checkpoints and approval | A deep-agent specialist has an explicit name, scoped tools, and isolated context. |

## Walkthrough

Run commands from the repository root; the same commands work in PowerShell, macOS, and Linux. Open the source alongside the output. Find the state declaration, node functions, graph connections, and invocation. For a failure, start with the earliest changed field or scheduled node.

```text
uv run python modules/bonus/B2_deep_agents/examples/01_deep_agent_planning.py
```

**Predict, then run:** for {"first_status": "in_progress", "include_planning": true}, write the resulting fields and any expected error. Then test the boundary cases in tests/deep_agent_planning.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "todos": [
      {
        "content": "Read the policy deductible",
        "status": "in_progress"
      },
      {
        "content": "Review the contractor estimate",
        "status": "pending"
      }
    ],
    "tool_statuses": [
      "success"
    ],
    "final": "The policy and document investigation plan is recorded."
  }
}
```

create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. This pinned release uses explicit TodoListMiddleware for planning. The write_todos tool updates declared task state; marking an item completed is not evidence that the underlying investigation actually happened.

</details>

```text
uv run python modules/bonus/B2_deep_agents/examples/02_virtual_filesystem.py
```

**Predict, then run:** for {"path": "/claims/review.txt", "content": "Synthetic estimate requires review."}, write the resulting fields and any expected error. Then test the boundary cases in tests/virtual_filesystem.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "paths": [
      "/claims/review.txt"
    ],
    "contents": {
      "/claims/review.txt": "Synthetic estimate requires review."
    },
    "tool_statuses": [
      "success"
    ]
  }
}
```

StateBackend stores a virtual filesystem in graph state instead of writing host files. Typed FilesystemPermission rules restrict writes to the claim directory, and checkpoints retain the resulting artifact. Tool success is checked separately from the final model sentence: a scripted acknowledgment cannot prove a denied write happened.

</details>

```text
uv run python modules/bonus/B2_deep_agents/examples/03_deep_subagents.py
```

**Predict, then run:** for {"decision": "approve", "specialist": "policy_expert"}, write the resulting fields and any expected error. Then test the boundary cases in tests/deep_subagents.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "paused": 1,
    "tool_results": [
      "The synthetic deductible is 100000 cents."
    ],
    "final": "The delegation request is complete."
  }
}
```

A deep-agent specialist has an explicit name, scoped tools, and isolated context. Delegation itself is gated by human approval and the parent has a model-call budget. The specialist receives a narrow policy question rather than the whole customer file. A rejected delegation must not execute the specialist task.

</details>

When build_graph needs no arguments, its generated Mermaid diagram is saved beside the example. A diagram records possible edges; a runtime stream records executed work. A single sequence advances one node per superstep. Parallel nodes see the same previous boundary, so they cannot read a sibling's unfinished update.

## When to use it, and when not to

Use these contracts when the claim needs the state or control-flow behavior described above. Keep pure arithmetic and validation in ordinary functions that can be tested independently. A graph, checkpoint, or extra agent adds operational choices; justify it with a concrete failure, pause, branch, or reuse requirement.

## Real-world use case

Plan a larger claim investigation using explicit planning and bounded subagents. The executable milestone uses only fictional records and the shared v11 implementation. [Read the use case](use_case/claims_copilot.py).

```text
uv run python modules/bonus/B2_deep_agents/use_case/claims_copilot.py
```

Sample output from the synthetic default case:

```json
{
  "paused": 1,
  "tool_results": [
    "The synthetic deductible is 100000 cents."
  ],
  "final": "The delegation request is complete."
}
```

A real team would connect this boundary to validated records and authenticated roles, then retain the same rejection, ownership, and recovery checks.

## Common bugs

| Symptom or broken contract | Cause and repair | Practice |
| --- | --- | --- |
| Observed `{"error": "ValueError"}`. Install the explicit planning middleware when requested. | Restore `[TodoListMiddleware()] if case["include_planning"] else []` and check the boundary cases. | [B2-01](../../../gym/tasks/B2/B2-01_deep_agent_planning_build/task.md) |
| Observed `{"value": {"todos": [{"content": "Read the policy deductible", "status": "completed"}, {"content": "Review the contractor estimate", "status": "pending"}], "tool_statuses": ["success"], "final": "The policy and document `. Keep task progress consistent with the supplied status. | Restore `"status": case["first_status"]` and check the boundary cases. | [B2-02](../../../gym/tasks/B2/B2-02_deep_agent_planning_fix/task.md) |
| Observed `{"value": {"paths": [], "contents": {}, "tool_statuses": ["error"]}}`. Allow the explicitly scoped claim artifact path. | Restore `paths=["/claims/**"], mode="allow"` and check the boundary cases. | [B2-07](../../../gym/tasks/B2/B2-07_virtual_filesystem_build/task.md) |
| Observed `{"value": {"paths": ["/claims/review.txt"], "contents": {"/claims/review.txt": "Synthetic estimate requires review."}, "tool_statuses": ["success"]}}`. Deny writes outside the permitted virtual directory. | Restore `paths=["/**"], mode="deny"` and check the boundary cases. | [B2-08](../../../gym/tasks/B2/B2-08_virtual_filesystem_fix/task.md) |
| Observed `{"value": {"paused": 1, "tool_results": ["We cannot invoke subagent missing_specialist because it does not exist, the only allowed types are `general-purpose`, `policy_expert`"], "final": "The delegation request is compl`. Delegate to the explicitly registered specialist. | Restore `"subagent_type": case["specialist"]` and check the boundary cases. | [B2-13](../../../gym/tasks/B2/B2-13_deep_subagents_build/task.md) |
| Observed `{"value": {"paused": 1, "tool_results": ["The synthetic deductible is 100000 cents."], "final": "The delegation request is complete."}}`. Preserve a human rejection of delegation. | Restore `decision = {"type": case["decision"]}` and check the boundary cases. | [B2-14](../../../gym/tasks/B2/B2-14_deep_subagents_fix/task.md) |

## Practice

- [B2-01 — build, easy](../../../gym/tasks/B2/B2-01_deep_agent_planning_build/task.md): Build deep agent planning: Install the explicit planning middleware when requested.
- [B2-02 — fix, medium](../../../gym/tasks/B2/B2-02_deep_agent_planning_fix/task.md): Fix deep agent planning: Keep task progress consistent with the supplied status.
- [B2-03 — predict, easy](../../../gym/tasks/B2/B2-03_deep_agent_planning_predict/task.md): Predict deep agent planning across the declared cases
- [B2-04 — trace, medium](../../../gym/tasks/B2/B2-04_deep_agent_planning_trace/task.md): Trace deep agent planning: Keep task progress consistent with the supplied status.
- [B2-05 — extend, hard](../../../gym/tasks/B2/B2-05_deep_agent_planning_extend/task.md): Extend deep agent planning: Do not mark unstarted document review as completed.
- [B2-06 — refactor, hard](../../../gym/tasks/B2/B2-06_deep_agent_planning_refactor/task.md): Refactor deep agent planning: Call the registered planning capability.
- [B2-07 — build, easy](../../../gym/tasks/B2/B2-07_virtual_filesystem_build/task.md): Build virtual filesystem: Allow the explicitly scoped claim artifact path.
- [B2-08 — fix, medium](../../../gym/tasks/B2/B2-08_virtual_filesystem_fix/task.md): Fix virtual filesystem: Deny writes outside the permitted virtual directory.
- [B2-09 — predict, easy](../../../gym/tasks/B2/B2-09_virtual_filesystem_predict/task.md): Predict virtual filesystem across the declared cases
- [B2-10 — trace, medium](../../../gym/tasks/B2/B2-10_virtual_filesystem_trace/task.md): Trace virtual filesystem: Deny writes outside the permitted virtual directory.
- [B2-11 — extend, hard](../../../gym/tasks/B2/B2-11_virtual_filesystem_extend/task.md): Extend virtual filesystem: Persist the supplied investigation note without substitution.
- [B2-12 — refactor, hard](../../../gym/tasks/B2/B2-12_virtual_filesystem_refactor/task.md): Refactor virtual filesystem: Honor and validate the requested virtual artifact path.
- [B2-13 — build, easy](../../../gym/tasks/B2/B2-13_deep_subagents_build/task.md): Build deep subagents: Delegate to the explicitly registered specialist.
- [B2-14 — fix, medium](../../../gym/tasks/B2/B2-14_deep_subagents_fix/task.md): Fix deep subagents: Preserve a human rejection of delegation.
- [B2-15 — predict, easy](../../../gym/tasks/B2/B2-15_deep_subagents_predict/task.md): Predict deep subagents across the declared cases
- [B2-16 — trace, medium](../../../gym/tasks/B2/B2-16_deep_subagents_trace/task.md): Trace deep subagents: Preserve a human rejection of delegation.
- [B2-17 — extend, hard](../../../gym/tasks/B2/B2-17_deep_subagents_extend/task.md): Extend deep subagents: Keep the specialist's evidence answer tied to the policy fixture.
- [B2-18 — design, hard](../../../gym/tasks/B2/B2-18_deep_subagents_design/task.md): Design deep subagents and justify the boundary policies

Start with tasks 01, 02, 09, 10, 17, and 18 in this module. Finish the other tasks for full practice. Hints are progressive; solution exposure is recorded. Predict and Trace tasks use answer JSON, not a code starter.

## Quiz

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

## Cost and safety

The default commands cost $0: deterministic Python and, in model lessons, scripted local fakes. They consume no hosted tokens and make no real payments or emails. Optional live experiments use the provider configured in .env; a short one-to-four-call exercise is usually cents, but verify your provider's current token prices and set a budget. Ollama can run locally without a hosted bill. Temporary checkpoint files are isolated from the committed dataset. Keep real customer details and credentials out of graph state.

## Key takeaways

- State visibility and update rules determine what a node can safely assume.
- Check normal, missing, boundary, and failure cases before trusting a workflow.
- Separate observed execution from diagrams, predictions, and durable history.
- Model output is evidence to validate, never an authorization grant.
- A saved checkpoint and an external effect have separate durability boundaries.

## Go deeper

- [deep agent planning official guide](https://docs.langchain.com/oss/python/deepagents/overview)
- [virtual filesystem official guide](https://docs.langchain.com/oss/python/deepagents/backends)
- [deep subagents official guide](https://docs.langchain.com/oss/python/deepagents/subagents)

## Next:

Continue to [module B3: Build a mini-LangGraph](../../../modules/bonus/B3_mini_langgraph/README.md).
