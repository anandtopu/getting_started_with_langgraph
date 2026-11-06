# 16-04 — Trace api boundaries: Honor the bounded retry allowance after a lost acknowledgment.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

async def creates a coroutine; await lets other work proceed while a request waits. An injected HTTP transport makes failures testable without a server. Retry only transient transport failures, bound attempts and timeouts, and reuse a stable idempotency key because a missing acknowledgment may follow a successful write.

## Your task

Honor the bounded retry allowance after a lost acknowledgment. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 16-04
uv run gym check 16-04
uv run gym hint 16-04
```

## Reading

[Module lesson](../../../../modules/16_external_systems_and_mcp/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
