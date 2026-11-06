# B4-07 — Build delta channels beta: Retain earlier delta writes when applying a new batch.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Beta DeltaChannel stores incremental writes and reconstructs channel state through a deterministic batch reducer. snapshot_frequency bounds how often a full snapshot is written. The reducer must be invariant to regrouping write batches, because replay may batch differently from live execution. Schema and reducer changes require migration testing before reusing old threads.

## Your task

Retain earlier delta writes when applying a new batch. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "notes": [
      "intake",
      "policy",
      "estimate"
    ],
    "snapshot_frequency": 2
  },
  {
    "notes": [
      "intake",
      "policy",
      "estimate"
    ],
    "snapshot_frequency": 1
  },
  {
    "notes": [],
    "snapshot_frequency": 2
  },
  {
    "notes": [
      "intake",
      "policy",
      "estimate"
    ],
    "snapshot_frequency": 0
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B4-07
uv run gym check B4-07
uv run gym hint B4-07
```

## Reading

[Module lesson](../../../../modules/bonus/B4_whats_new/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
