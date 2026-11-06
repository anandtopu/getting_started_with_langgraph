# B2-16 — Trace deep subagents: Preserve a human rejection of delegation.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A deep-agent specialist has an explicit name, scoped tools, and isolated context. Delegation itself is gated by human approval and the parent has a model-call budget. The specialist receives a narrow policy question rather than the whole customer file. A rejected delegation must not execute the specialist task.

## Your task

Preserve a human rejection of delegation. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "decision": "approve",
    "specialist": "policy_expert"
  },
  {
    "decision": "reject",
    "specialist": "policy_expert"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-16
uv run gym check B2-16
uv run gym hint B2-16
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/subagents)
