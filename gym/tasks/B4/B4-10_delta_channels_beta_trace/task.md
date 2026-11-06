# B4-10 — Trace delta channels beta: Honor and validate the requested snapshot cadence.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Beta DeltaChannel stores incremental writes and reconstructs channel state through a deterministic batch reducer. snapshot_frequency bounds how often a full snapshot is written. The reducer must be invariant to regrouping write batches, because replay may batch differently from live execution. Schema and reducer changes require migration testing before reusing old threads.

## Your task

Honor and validate the requested snapshot cadence. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B4-10
uv run gym check B4-10
uv run gym hint B4-10
```

## Reading

[Module lesson](../../../../modules/bonus/B4_whats_new/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
