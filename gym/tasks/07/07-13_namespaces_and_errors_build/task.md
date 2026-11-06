# 07-13 — Build namespaces and errors: Nested updates require subgraph streaming.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A subgraph namespace identifies nested work. Sibling parallel events can arrive in either order; causal requirements, such as summary after both checks, are stable. A live event trace is not itself the durable checkpoint history.

## Your task

Nested updates require subgraph streaming. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001"
  },
  {
    "claim_id": "CLM-0101"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 07-13
uv run gym check 07-13
uv run gym hint 07-13
```

## Reading

[Module lesson](../../../../modules/07_time_travel_and_streaming/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
