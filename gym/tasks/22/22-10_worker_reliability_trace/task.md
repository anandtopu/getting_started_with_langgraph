# 22-10 — Diagnose worker reliability from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Stateless workers share durable checkpoints, ownership records, and effect keys. One active run may mutate a thread at a time. The local registry demonstrates lease exclusion within one process; the Postgres implementation uses a transaction-scoped advisory lock across workers. A new ledger instance proves that idempotency survives worker replacement, and conflicting payloads are rejected.

## Your task

Diagnose worker reliability from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Use the same business effect identity after worker replacement."
- "Report that a competing run was excluded."
- "Exercise and reject idempotency-key reuse with a changed payload."
- "Read the persisted effect count from the restarted worker's ledger."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-10
uv run gym check 22-10
uv run gym hint 22-10
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
