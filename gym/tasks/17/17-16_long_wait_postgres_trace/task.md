# 17-16 — Diagnose long wait postgres from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An interrupt persists a wait without holding a worker open. The simulated receipt date advances three days while the program itself finishes immediately. Reopening the SQLite saver proves connection-lifetime independence. The same graph includes synchronous and asynchronous Postgres variants; schema setup belongs in startup or migrations, not each request.

## Your task

Diagnose long wait postgres from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "received_on": "2026-01-04",
    "document_id": "DOC-001"
  },
  {
    "claim_id": "CLM-0001",
    "received_on": "2026-01-01",
    "document_id": "DOC-001"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Reject a receipt date earlier than the request date."
- "Compute elapsed business time from explicit dates."
- "Require the missing document before ending the durable wait."
- "Preserve the received evidence identifier on resume."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 17-16
uv run gym check 17-16
uv run gym hint 17-16
```

## Reading

[Module lesson](../../../../modules/17_durable_execution/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
