# 14-10 — Diagnose handoffs from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Command.PARENT transfers control from a child graph to a node in its parent. The shared messages channel uses add_messages. A tool-based handoff includes both the AI request and its ToolMessage acknowledgment so the next specialist receives a valid conversation. Parent destinations must not be declared as local child nodes.

## Your task

Diagnose handoffs from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "question": "Explain the deductible."
  },
  {
    "claim_id": "CLM-0400",
    "question": "What is the water deductible?"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Address the parent graph when handing off to its specialist."
- "Pair the handoff acknowledgment with its AI request."
- "Update ownership together with the handoff."
- "Forward the complete handoff pair."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 14-10
uv run gym check 14-10
uv run gym hint 14-10
```

## Reading

[Module lesson](../../../../modules/14_multi_agent_systems/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs)
