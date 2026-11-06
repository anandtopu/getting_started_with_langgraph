# 22-16 — Trace managed deployment: Keep interactive waiting distinct from background execution.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An assistant selects graph configuration, a thread identifies persisted state, and a run is one execution. Agent Server supports background runs; LangSmith Deployment adds managed hosting and scheduled jobs subject to account access and current pricing. This offline request planner creates no hosted resources. The explicit SDK function requires a caller-supplied authenticated client and full graph input.

## Your task

Keep interactive waiting distinct from background execution. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-16
uv run gym check 22-16
uv run gym hint 22-16
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/deploy)
