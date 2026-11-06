# B3-04 — Trace channels and steps: Report the previous-boundary view seen by each worker.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

The educational runner snapshots state before a superstep, collects writes from every sibling, then applies them at a barrier. Thus both workers see zero prior findings while the next-step summary sees both. This small runner explains visibility; it deliberately omits production concurrency, async execution, pending-write recovery, and serialization.

## Your task

Report the previous-boundary view seen by each worker. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-04
uv run gym check B3-04
uv run gym hint B3-04
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/pregel)
