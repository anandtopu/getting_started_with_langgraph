# 05-16 — Trace inspect checkpoints: Continue the configuration returned by update_state, not an unrelated checkpoint.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A StateSnapshot contains values, pending next nodes, metadata, and a parent configuration. update_state writes a new checkpoint; it does not edit old history. Durability chooses when checkpoint writes complete, which changes failure exposure rather than business routing.

## Your task

Continue the configuration returned by update_state, not an unrelated checkpoint. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-16
uv run gym check 05-16
uv run gym hint 05-16
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
