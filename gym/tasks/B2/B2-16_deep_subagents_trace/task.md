# B2-16 — Diagnose deep subagents from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A deep-agent specialist has an explicit name, scoped tools, and isolated context. Delegation itself is gated by human approval and the parent has a model-call budget. The specialist receives a narrow policy question rather than the whole customer file. A rejected delegation must not execute the specialist task.

## Your task

Diagnose deep subagents from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Delegate to the explicitly registered specialist."
- "Preserve a human rejection of delegation."
- "Keep the specialist's evidence answer tied to the policy fixture."
- "Allow the bounded model operations needed to complete an approved delegation."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B2-16
uv run gym check B2-16
uv run gym hint B2-16
```

## Reading

[Module lesson](../../../../modules/bonus/B2_deep_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/deepagents/subagents)
