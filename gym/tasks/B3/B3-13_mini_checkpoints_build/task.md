# B3-13 — Build mini checkpoints: Preserve rejection when resuming the waiting teaching thread.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A checkpoint stores state and the next scheduled work for one thread. The mini runner copies snapshots so external mutation cannot corrupt history. Its single-node pause records a request and resumes the same pending node with a checked decision; another thread remains independent. This is a teaching representation, not LangGraph's full interrupt protocol.

## Your task

Preserve rejection when resuming the waiting teaching thread. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-13
uv run gym check B3-13
uv run gym hint B3-13
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
