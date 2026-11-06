# 22-15 — Predict managed deployment across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

An assistant selects graph configuration, a thread identifies persisted state, and a run is one execution. Agent Server supports background runs; LangSmith Deployment adds managed hosting and scheduled jobs subject to account access and current pricing. This offline request planner creates no hosted resources. The explicit SDK function requires a caller-supplied authenticated client and full graph input.

## Your task

Predict managed deployment across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-15
uv run gym check 22-15
uv run gym hint 22-15
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/deploy)
