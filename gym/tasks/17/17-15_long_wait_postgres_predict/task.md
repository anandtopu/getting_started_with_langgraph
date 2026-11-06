# 17-15 — Predict long wait postgres across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

An interrupt persists a wait without holding a worker open. The simulated receipt date advances three days while the program itself finishes immediately. Reopening the SQLite saver proves connection-lifetime independence. The same graph includes synchronous and asynchronous Postgres variants; schema setup belongs in startup or migrations, not each request.

## Your task

Predict long wait postgres across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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
  },
  {
    "claim_id": "CLM-0001",
    "received_on": "2025-12-31",
    "document_id": "DOC-001"
  },
  {
    "claim_id": "CLM-0001",
    "received_on": "2026-01-04",
    "document_id": ""
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 17-15
uv run gym check 17-15
uv run gym hint 17-15
```

## Reading

[Module lesson](../../../../modules/17_durable_execution/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
