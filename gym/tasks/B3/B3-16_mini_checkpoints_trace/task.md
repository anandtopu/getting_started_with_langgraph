# B3-16 — Trace mini checkpoints: Validate the resumed decision before updating approval state.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A checkpoint stores state and the next scheduled work for one thread. The mini runner copies snapshots so external mutation cannot corrupt history. Its single-node pause records a request and resumes the same pending node with a checked decision; another thread remains independent. This is a teaching representation, not LangGraph's full interrupt protocol.

## Your task

Validate the resumed decision before updating approval state. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-16
uv run gym check B3-16
uv run gym hint B3-16
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
