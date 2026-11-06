# B4-04 — Diagnose event streaming beta from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Beta v3 event streaming exposes typed message, subgraph, value, and output projections. Child messages belong to the subgraph projection. The raw protocol uses method and params rather than the v2 type/ns/data shape. This example uses a fresh fake run for raw-event inspection so consuming one view does not pretend to replay already-consumed events.

## Your task

Diagnose event streaming beta from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Read child model messages through their subgraph projection."
- "Read the final model message from the completed output projection."
- "Consume the raw protocol when inspecting lifecycle channels."
- "Use the v3 protocol namespace location rather than a guessed field."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B4-04
uv run gym check B4-04
uv run gym hint B4-04
```

## Reading

[Module lesson](../../../../modules/bonus/B4_whats_new/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/event-streaming)
