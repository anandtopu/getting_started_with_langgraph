# 05-09 — Predict sqlite lifetime across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Memory persistence ends with its process. A SQLite saver stores checkpoints on disk and must remain open for every invocation that uses it. Explicit context managers release connections, including on Windows where open files can prevent cleanup.

## Your task

Predict sqlite lifetime across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001"
  },
  {
    "claim_id": "CLM-0199"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-09
uv run gym check 05-09
uv run gym hint 05-09
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
