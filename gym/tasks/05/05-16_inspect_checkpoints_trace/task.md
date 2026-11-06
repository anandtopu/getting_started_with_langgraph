# 05-16 — Diagnose inspect checkpoints from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A StateSnapshot contains values, pending next nodes, metadata, and a parent configuration. update_state writes a new checkpoint; it does not edit old history. Durability chooses when checkpoint writes complete, which changes failure exposure rather than business routing.

## Your task

Diagnose inspect checkpoints from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "amount_cents": 100000,
    "corrected_amount": 200000,
    "durability": "sync"
  },
  {
    "amount_cents": 200000,
    "corrected_amount": 50000,
    "durability": "sync"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "The corrected checkpoint must contain the replacement evidence."
- "Continue the configuration returned by update_state, not an unrelated checkpoint."
- "The edit attribution determines the pending successor nodes."
- "Present logical step order explicitly instead of relying on history arrival order."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-16
uv run gym check 05-16
uv run gym hint 05-16
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
