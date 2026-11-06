# 03-04 — Diagnose conditional router from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A routing function chooses a label from current state. A path map connects that label to a real node. A total router has an outcome for every accepted input, including zero, missing evidence, unknown categories, and malformed amounts.

## Your task

Diagnose conditional router from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "claim_type": "water",
    "amount_cents": 100000,
    "missing": []
  },
  {
    "claim_type": "water",
    "amount_cents": 100001,
    "missing": []
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "The exact fast-track threshold is inclusive."
- "Path-map values must match each intended destination."
- "High-value claims require specialist review."
- "Refactoring must retain the missing-evidence route."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 03-04
uv run gym check 03-04
uv run gym hint 03-04
```

## Reading

[Module lesson](../../../../modules/03_branching_and_routing/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-control-flow)
