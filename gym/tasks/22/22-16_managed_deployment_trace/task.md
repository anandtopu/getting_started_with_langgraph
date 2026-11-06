# 22-16 — Diagnose managed deployment from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An assistant selects graph configuration, a thread identifies persisted state, and a run is one execution. Agent Server supports background runs; LangSmith Deployment adds managed hosting and scheduled jobs subject to account access and current pricing. This offline request planner creates no hosted resources. The explicit SDK function requires a caller-supplied authenticated client and full graph input.

## Your task

Diagnose managed deployment from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Require both assistant configuration and thread identity."
- "Keep interactive waiting distinct from background execution."
- "Reject an obviously malformed schedule before proposing a hosted job."
- "Do not substitute assistant identity for thread identity."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 22-16
uv run gym check 22-16
uv run gym hint 22-16
```

## Reading

[Module lesson](../../../../modules/22_deployment/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/deploy)
