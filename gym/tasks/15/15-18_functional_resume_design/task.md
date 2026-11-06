# 15-18 — Design functional resume and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Resuming a Functional API interrupt restarts the entrypoint from its beginning. Completed task results are retrieved from checkpoints, so the task body need not run again. Keep task ordering deterministic and validate the resume payload. External effects still require their own idempotency at the crash window.

## Your task

Design functional resume and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

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
    "claim_id": "CLM-0001",
    "approved": "yes"
  },
  {
    "claim_id": "CLM-0077",
    "approved": true
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 15-18
uv run gym check 15-18
uv run gym hint 15-18
```

## Reading

[Module lesson](../../../../modules/15_functional_api/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/functional-api)
