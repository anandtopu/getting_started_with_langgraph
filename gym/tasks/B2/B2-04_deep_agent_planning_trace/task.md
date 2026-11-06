# B2-04 — Diagnose deep agent planning from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. This pinned release uses explicit TodoListMiddleware for planning. The write_todos tool updates declared task state; marking an item completed is not evidence that the underlying investigation actually happened.

## Your task

Diagnose deep agent planning from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "first_status": "in_progress",
    "include_planning": true
  },
  {
    "first_status": "completed",
    "include_planning": true
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Install the explicit planning middleware when requested."
- "Keep task progress consistent with the supplied status."
- "Do not mark unstarted document review as completed."
- "Call the registered planning capability."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-04
uv run gym check B2-04
uv run gym hint B2-04
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/overview)
