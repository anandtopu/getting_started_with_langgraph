# B3-04 — Diagnose channels and steps from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

The educational runner snapshots state before a superstep, collects writes from every sibling, then applies them at a barrier. Thus both workers see zero prior findings while the next-step summary sees both. This small runner explains visibility; it deliberately omits production concurrency, async execution, pending-write recovery, and serialization.

## Your task

Diagnose channels and steps from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "documents": [
      "estimate",
      "receipt"
    ]
  },
  {
    "documents": []
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Merge all sibling findings at the barrier."
- "Report the previous-boundary view seen by each worker."
- "Run the summary even when the document fan-out is empty."
- "Compute the summary from the merged findings."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-04
uv run gym check B3-04
uv run gym hint B3-04
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/pregel)
