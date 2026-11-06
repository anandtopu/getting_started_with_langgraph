# B3-01 — Build channels and steps: Merge all sibling findings at the barrier.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

The educational runner snapshots state before a superstep, collects writes from every sibling, then applies them at a barrier. Thus both workers see zero prior findings while the next-step summary sees both. This small runner explains visibility; it deliberately omits production concurrency, async execution, pending-write recovery, and serialization.

## Your task

Merge all sibling findings at the barrier. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B3-01
uv run gym check B3-01
uv run gym hint B3-01
```

## Reading

[Module lesson](../../../../modules/bonus/B3_mini_langgraph/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/pregel)
