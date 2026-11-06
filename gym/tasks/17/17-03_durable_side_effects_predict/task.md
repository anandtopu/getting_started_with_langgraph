# 17-03 — Predict durable side effects across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A task result is reusable only after it is checkpointed. This example kills an owned child after the effect ledger commits but before the task returns, then starts a new process. A payload-bound idempotency key prevents duplicate effects even in that gap. sync, async, and exit durability offer different checkpoint guarantees; none makes an external system transactional with the graph.

## Your task

Predict durable side effects across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "durability": "sync"
  },
  {
    "claim_id": "CLM-0001",
    "durability": "async"
  },
  {
    "claim_id": "CLM-0001",
    "durability": "exit"
  },
  {
    "claim_id": "CLM-0050",
    "durability": "sync"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 17-03
uv run gym check 17-03
uv run gym hint 17-03
```

## Reading

[Module lesson](../../../../modules/17_durable_execution/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
