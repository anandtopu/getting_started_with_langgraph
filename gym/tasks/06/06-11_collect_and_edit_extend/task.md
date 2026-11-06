# 06-11 — Extend collect and edit: Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Parallel pauses can be answered with an interrupt-ID-to-response map. IDs identify requests; list order does not. Validate each edited value against its own schema and business limit before merging it into state.

## Your task

Add run_batch(cases) to preview independent claims in input order. Preserve run(case), isolate mutable inputs, return value/error records, handle an empty batch, and continue after a rejected claim. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "loss_date": "2026-01-01",
    "approved_cents": 125000
  },
  {
    "loss_date": "2026-01-01",
    "approved_cents": 0
  },
  {
    "loss_date": "2026-01-01",
    "approved_cents": 500001
  },
  {
    "loss_date": "invalid",
    "approved_cents": 125000
  },
  {
    "loss_date": "2026-01-01",
    "approved_cents": true
  }
]
```

The new capability is checked in addition to the original cases. For run_batch, edit the Python orchestration interface (including in the TypeScript bonus); leave run(case) behavior intact. A batch is sequential and each case owns a new workflow invocation, not a shared durable thread.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-11
uv run gym check 06-11
uv run gym hint 06-11
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
