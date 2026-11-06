# 14-04 — Diagnose supervisor tools from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A supervisor may call specialists as tools. Each specialist gets a narrow evidence prompt and a private message history; the supervisor receives only the returned conclusion. This direct create_agent pattern avoids an extra helper package. More agents add calls and failure boundaries, so compare them against a single-agent baseline.

## Your task

Diagnose supervisor tools from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "question": "Review policy and fraud evidence.",
    "private_note": "Synthetic phone: 555-0100"
  },
  {
    "question": "Which document is missing?",
    "private_note": "Synthetic address withheld"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Register both specialist capabilities with the supervisor."
- "Keep specialist roles attached to the evidence they reviewed."
- "Give the policy specialist authoritative scoped evidence."
- "Return the specialist conclusion instead of its input prompt."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 14-04
uv run gym check 14-04
uv run gym hint 14-04
```

## Reading

[Module lesson](../../../../modules/14_multi_agent_systems/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)
