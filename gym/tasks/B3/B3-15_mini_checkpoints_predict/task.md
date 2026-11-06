# B3-15 — Predict mini checkpoints across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A checkpoint stores state and the next scheduled work for one thread. The mini runner copies snapshots so external mutation cannot corrupt history. Its single-node pause records a request and resumes the same pending node with a checked decision; another thread remains independent. This is a teaching representation, not LangGraph's full interrupt protocol.

## Your task

Predict mini checkpoints across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "approved": false,
    "claim_id": "CLM-0001"
  },
  {
    "approved": true,
    "claim_id": "CLM-0001"
  },
  {
    "approved": "yes",
    "claim_id": "CLM-0001"
  },
  {
    "approved": false,
    "claim_id": "CLM-0010"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-15
uv run gym check B3-15
uv run gym hint B3-15
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
