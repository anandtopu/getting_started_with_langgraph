# B3-16 — Diagnose mini checkpoints from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A checkpoint stores state and the next scheduled work for one thread. The mini runner copies snapshots so external mutation cannot corrupt history. Its single-node pause records a request and resumes the same pending node with a checked decision; another thread remains independent. This is a teaching representation, not LangGraph's full interrupt protocol.

## Your task

Diagnose mini checkpoints from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Preserve rejection when resuming the waiting teaching thread."
- "Validate the resumed decision before updating approval state."
- "Read the archived snapshot rather than an externally modified copy."
- "Inspect the other thread independently after completing the first."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-16
uv run gym check B3-16
uv run gym hint B3-16
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
