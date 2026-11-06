# 03-16 — Diagnose early exit from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Termination is a routing outcome, not an exceptional Python crash. Screen invalid and duplicate claims before assigning work. The returned state should still explain why a claim ended so an adjuster can inspect it.

## Your task

Diagnose early exit from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "amount_cents": 0,
    "duplicate_of": null
  },
  {
    "claim_id": "CLM-0001",
    "amount_cents": -1,
    "duplicate_of": null
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Rejected claims must stop before assignment."
- "Zero is a defined boundary, not an omitted case."
- "Duplicate submissions need an explicit terminal reason."
- "Preserve eligible-case behavior while refactoring routes."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-16
uv run gym check 03-16
uv run gym hint 03-16
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
