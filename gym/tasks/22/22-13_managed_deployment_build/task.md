# 22-13 — Build managed deployment: Require both assistant configuration and thread identity.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

An assistant selects graph configuration, a thread identifies persisted state, and a run is one execution. Agent Server supports background runs; LangSmith Deployment adds managed hosting and scheduled jobs subject to account access and current pricing. This offline request planner creates no hosted resources. The explicit SDK function requires a caller-supplied authenticated client and full graph input.

## Your task

Require both assistant configuration and thread identity. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "assistant_id": "claims",
    "thread_id": "claim-thread",
    "schedule": "0 9 * * 1-5",
    "background": true
  },
  {
    "assistant_id": "claims",
    "thread_id": "claim-thread",
    "schedule": "0 9 * * 1-5",
    "background": false
  },
  {
    "assistant_id": "",
    "thread_id": "claim-thread",
    "schedule": "0 9 * * 1-5",
    "background": true
  },
  {
    "assistant_id": "claims",
    "thread_id": "claim-thread",
    "schedule": "invalid",
    "background": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-13
uv run gym check 22-13
uv run gym hint 22-13
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/deploy)
