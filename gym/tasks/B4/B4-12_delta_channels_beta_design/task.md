# B4-12 — Design delta channels beta and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Beta DeltaChannel stores incremental writes and reconstructs channel state through a deterministic batch reducer. snapshot_frequency bounds how often a full snapshot is written. The reducer must be invariant to regrouping write batches, because replay may batch differently from live execution. Schema and reducer changes require migration testing before reusing old threads.

## Your task

Design delta channels beta and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B4-12
uv run gym check B4-12
uv run gym hint B4-12
```

## Reading

[Module lesson](../../../../modules/bonus/B4_whats_new/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api)
