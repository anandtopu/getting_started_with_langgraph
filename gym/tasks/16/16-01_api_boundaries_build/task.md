# 16-01 — Build api boundaries: Reuse the same idempotency key across a retry.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

async def creates a coroutine; await lets other work proceed while a request waits. An injected HTTP transport makes failures testable without a server. Retry only transient transport failures, bound attempts and timeouts, and reuse a stable idempotency key because a missing acknowledgment may follow a successful write.

## Your task

Reuse the same idempotency key across a retry. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "transient_failures": 1,
    "attempts": 3
  },
  {
    "claim_id": "CLM-0001",
    "transient_failures": 0,
    "attempts": 3
  },
  {
    "claim_id": "CLM-0001",
    "transient_failures": 4,
    "attempts": 3
  },
  {
    "claim_id": "CLM-0001",
    "transient_failures": 1,
    "attempts": 0
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 16-01
uv run gym check 16-01
uv run gym hint 16-01
```

## Reading

[Module lesson](../../../../modules/16_external_systems_and_mcp/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
