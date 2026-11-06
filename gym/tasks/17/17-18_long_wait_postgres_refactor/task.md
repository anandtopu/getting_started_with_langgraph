# 17-18 — Refactor long wait postgres: Preserve the received evidence identifier on resume.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

An interrupt persists a wait without holding a worker open. The simulated receipt date advances three days while the program itself finishes immediately. Reopening the SQLite saver proves connection-lifetime independence. The same graph includes synchronous and asynchronous Postgres variants; schema setup belongs in startup or migrations, not each request.

## Your task

Preserve the received evidence identifier on resume. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 17-18
uv run gym check 17-18
uv run gym hint 17-18
```

## Reading

[Module lesson](../../../../modules/17_durable_execution/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
