# 06-18 — Refactor safe reentry: Separate checkpointed work still needs an idempotent effect contract.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

On resume, Python starts the interrupted node again. Code before interrupt can therefore repeat. Move effects after validated approval into separate checkpointed work, and use a stable idempotency key because a crash can occur after a write but before its checkpoint.

## Your task

Separate checkpointed work still needs an idempotent effect contract. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "approved": true
  },
  {
    "claim_id": "CLM-0001",
    "approved": false
  },
  {
    "claim_id": "CLM-0041",
    "approved": true
  },
  {
    "claim_id": "CLM-0001",
    "approved": "yes"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-18
uv run gym check 06-18
uv run gym hint 06-18
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
