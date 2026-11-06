# 05-14 — Fix inspect checkpoints: Continue the configuration returned by update_state, not an unrelated checkpoint.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A StateSnapshot contains values, pending next nodes, metadata, and a parent configuration. update_state writes a new checkpoint; it does not edit old history. Durability chooses when checkpoint writes complete, which changes failure exposure rather than business routing.

## Your task

Continue the configuration returned by update_state, not an unrelated checkpoint. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-14
uv run gym check 05-14
uv run gym hint 05-14
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
