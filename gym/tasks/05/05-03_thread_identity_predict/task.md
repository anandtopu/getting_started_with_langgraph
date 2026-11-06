# 05-03 — Predict thread identity across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A checkpointer saves graph state under a thread ID. New input on that thread starts another run against its saved state. Resuming a pending operation is different: use the saved continuation or an interrupt response rather than pretending it is a new claim.

## Your task

Predict thread identity across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "first_id": "CLM-0001",
    "second_id": "CLM-0002"
  },
  {
    "first_id": "CLM-A",
    "second_id": "CLM-B"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-03
uv run gym check 05-03
uv run gym hint 05-03
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
