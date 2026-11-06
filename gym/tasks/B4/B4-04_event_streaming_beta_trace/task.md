# B4-04 — Trace event streaming beta: Read the final model message from the completed output projection.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Beta v3 event streaming exposes typed message, subgraph, value, and output projections. Child messages belong to the subgraph projection. The raw protocol uses method and params rather than the v2 type/ns/data shape. This example uses a fresh fake run for raw-event inspection so consuming one view does not pretend to replay already-consumed events.

## Your task

Read the final model message from the completed output projection. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "text": "Synthetic claim review is complete."
  },
  {
    "text": "Estimate accepted for review."
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B4-04
uv run gym check B4-04
uv run gym hint B4-04
```

## Reading

[Module lesson](../../../../modules/bonus/B4_whats_new/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/event-streaming)
