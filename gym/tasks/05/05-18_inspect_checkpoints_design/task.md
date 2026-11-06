# 05-18 — Design inspect checkpoints and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A StateSnapshot contains values, pending next nodes, metadata, and a parent configuration. update_state writes a new checkpoint; it does not edit old history. Durability chooses when checkpoint writes complete, which changes failure exposure rather than business routing.

## Your task

Design inspect checkpoints and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

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
  },
  {
    "amount_cents": 100000,
    "corrected_amount": 200000,
    "durability": "async"
  },
  {
    "amount_cents": 100000,
    "corrected_amount": 200000,
    "durability": "exit"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-18
uv run gym check 05-18
uv run gym hint 05-18
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
