# 03-16 — Trace early exit: Zero is a defined boundary, not an omitted case.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Termination is a routing outcome, not an exceptional Python crash. Screen invalid and duplicate claims before assigning work. The returned state should still explain why a claim ended so an adjuster can inspect it.

## Your task

Zero is a defined boundary, not an omitted case. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-16
uv run gym check 03-16
uv run gym hint 03-16
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
