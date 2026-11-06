# 13-15 — Predict subgraph persistence across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A parent checkpointer propagates into its child. A child compiled with the default per-invocation behavior starts fresh for each invocation; checkpointer=True gives the child persistent state across calls. While paused, get_state(subgraphs=True) exposes the nested task snapshot. Streaming namespaces identify which graph emitted an update.

## Your task

Predict subgraph persistence across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "approved": false,
    "persistent_child": false
  },
  {
    "claim_id": "CLM-0001",
    "approved": true,
    "persistent_child": false
  },
  {
    "claim_id": "CLM-0001",
    "approved": false,
    "persistent_child": true
  },
  {
    "claim_id": "CLM-0001",
    "approved": "yes",
    "persistent_child": false
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 13-15
uv run gym check 13-15
uv run gym hint 13-15
```

## Reading

[Module lesson](../../../../modules/13_subgraphs/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-subgraphs)
