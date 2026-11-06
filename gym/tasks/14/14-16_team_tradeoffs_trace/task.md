# 14-16 — Diagnose team tradeoffs from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A swarm-style team routes according to the active specialist, without requiring a central supervisor on every transition. Its business budget is distinct from the graph recursion limit. This controlled four-role comparison measures calls and completion; scripted answers do not establish that the team is smarter than the one-call baseline.

## Your task

Diagnose team tradeoffs from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "budget": 4,
    "start_agent": "intake"
  },
  {
    "budget": 2,
    "start_agent": "intake"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Stop delegation when the business call budget is exhausted."
- "Advance to the next specialist instead of handing work back to itself."
- "Count every specialist operation against the budget."
- "Mark successful completion when the final specialist finishes."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 14-16
uv run gym check 14-16
uv run gym hint 14-16
```

## Reading

[Module lesson](../../../../modules/14_multi_agent_systems/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/multi-agent)
