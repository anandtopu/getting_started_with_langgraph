# 22-07 — Build worker reliability: Use the same business effect identity after worker replacement.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Stateless workers share durable checkpoints, ownership records, and effect keys. One active run may mutate a thread at a time. The local registry demonstrates lease exclusion within one process; the Postgres implementation uses a transaction-scoped advisory lock across workers. A new ledger instance proves that idempotency survives worker replacement, and conflicting payloads are rejected.

## Your task

Use the same business effect identity after worker replacement. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "amount_cents": 50000,
    "changed_payload": false
  },
  {
    "claim_id": "CLM-0020",
    "amount_cents": 50000,
    "changed_payload": false
  },
  {
    "claim_id": "CLM-0001",
    "amount_cents": 50000,
    "changed_payload": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-07
uv run gym check 22-07
uv run gym hint 22-07
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
