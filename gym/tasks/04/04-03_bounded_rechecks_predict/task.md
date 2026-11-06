# 04-03 — Predict bounded rechecks across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A loop is an edge back to earlier work. Business state must move toward an exit. recursion_limit is a runtime backstop measured in graph steps, not a replacement for a document-recheck budget.

## Your task

Predict bounded rechecks across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "history": [
      false,
      false,
      true
    ],
    "budget": 3
  },
  {
    "history": [
      true
    ],
    "budget": 3
  },
  {
    "history": [
      false
    ],
    "budget": 2
  },
  {
    "history": [
      false,
      false,
      true
    ],
    "budget": 0
  },
  {
    "history": [
      false,
      false,
      false,
      false,
      false,
      false,
      false,
      false
    ],
    "budget": 8,
    "recursion_limit": 3
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-03
uv run gym check 04-03
uv run gym hint 04-03
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
