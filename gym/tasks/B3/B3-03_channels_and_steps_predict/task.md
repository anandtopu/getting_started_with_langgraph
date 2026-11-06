# B3-03 — Predict channels and steps across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

The educational runner snapshots state before a superstep, collects writes from every sibling, then applies them at a barrier. Thus both workers see zero prior findings while the next-step summary sees both. This small runner explains visibility; it deliberately omits production concurrency, async execution, pending-write recovery, and serialization.

## Your task

Predict channels and steps across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "documents": [
      "estimate"
    ]
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-03
uv run gym check B3-03
uv run gym hint B3-03
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/pregel)
