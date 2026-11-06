# 02-05 — Extend schema contracts: Preserve an optional loss date and its None default across all three schema styles.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

TypedDict describes a dictionary for type checking; it does not validate values at runtime. Dataclasses give attribute access and defaults. Pydantic checks fields at the boundary. With explicit v2 output, preserve the schema's object type before extracting its fields.

## Your task

Preserve an optional loss date and its None default across all three schema styles. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "kind": "pydantic",
    "amount_cents": 125000,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "typed",
    "amount_cents": 125000,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "dataclass",
    "amount_cents": 125000,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "pydantic",
    "amount_cents": -1,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "pydantic",
    "amount_cents": true,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "typed",
    "amount_cents": 0,
    "claim_id": "CLM-0001"
  },
  {
    "kind": "dataclass",
    "amount_cents": 125000,
    "claim_id": "CLM-0001",
    "loss_date": "2026-02-01"
  },
  {
    "kind": "typed",
    "amount_cents": 125000,
    "claim_id": "CLM-0001",
    "loss_date": null
  }
]
```

The new capability is checked in addition to the original cases. For run_batch, edit the Python orchestration interface (including in the TypeScript bonus); leave run(case) behavior intact. A batch is sequential and each case owns a new workflow invocation, not a shared durable thread.

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-05
uv run gym check 02-05
uv run gym hint 02-05
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
