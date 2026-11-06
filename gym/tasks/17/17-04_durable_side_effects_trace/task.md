# 17-04 — Trace durable side effects: Make the crash supervisor recognize the documented owned-worker exit.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A task result is reusable only after it is checkpointed. This example kills an owned child after the effect ledger commits but before the task returns, then starts a new process. A payload-bound idempotency key prevents duplicate effects even in that gap. sync, async, and exit durability offer different checkpoint guarantees; none makes an external system transactional with the graph.

## Your task

Make the crash supervisor recognize the documented owned-worker exit. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 17-04
uv run gym check 17-04
uv run gym hint 17-04
```

## Reading

[Module lesson](../../../../modules/17_durable_execution/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
