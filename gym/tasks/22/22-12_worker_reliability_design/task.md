# 22-12 — Design worker reliability and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Stateless workers share durable checkpoints, ownership records, and effect keys. One active run may mutate a thread at a time. The local registry demonstrates lease exclusion within one process; the Postgres implementation uses a transaction-scoped advisory lock across workers. A new ledger instance proves that idempotency survives worker replacement, and conflicting payloads are rejected.

## Your task

Design worker reliability and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-12
uv run gym check 22-12
uv run gym hint 22-12
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
