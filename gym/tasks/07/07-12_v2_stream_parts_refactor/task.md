# 07-12 — Refactor v2 stream parts: A unified dispatcher must preserve custom progress payloads.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A v2 stream part has type, ns, and data fields. Updates contain a node's changed fields; values contain the visible whole state; custom events carry application progress. Interrupt metadata is separate from ordinary values and must survive UI serialization.

## Your task

A unified dispatcher must preserve custom progress payloads. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "review": false
  },
  {
    "claim_id": "CLM-0001",
    "review": true
  },
  {
    "claim_id": "CLM-0040",
    "review": false
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 07-12
uv run gym check 07-12
uv run gym hint 07-12
```

## Reading

[Module lesson](../../../../modules/07_time_travel_and_streaming/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/streaming)
