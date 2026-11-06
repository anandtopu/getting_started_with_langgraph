# B2-04 — Trace deep agent planning: Keep task progress consistent with the supplied status.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. This pinned release uses explicit TodoListMiddleware for planning. The write_todos tool updates declared task state; marking an item completed is not evidence that the underlying investigation actually happened.

## Your task

Keep task progress consistent with the supplied status. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-04
uv run gym check B2-04
uv run gym hint B2-04
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/overview)
