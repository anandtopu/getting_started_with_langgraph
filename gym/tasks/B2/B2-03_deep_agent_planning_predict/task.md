# B2-03 — Predict deep agent planning across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

create_deep_agent supplies an agent harness, but current defaults should be inspected rather than remembered from older tutorials. This pinned release uses explicit TodoListMiddleware for planning. The write_todos tool updates declared task state; marking an item completed is not evidence that the underlying investigation actually happened.

## Your task

Predict deep agent planning across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "first_status": "in_progress",
    "include_planning": false
  },
  {
    "first_status": "invalid",
    "include_planning": true
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-03
uv run gym check B2-03
uv run gym hint B2-03
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/overview)
