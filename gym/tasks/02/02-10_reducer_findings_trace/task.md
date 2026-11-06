# 02-10 — Diagnose reducer findings from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A channel is one state field together with its update rule. The default rule overwrites. An Annotated reducer combines the old and new values. Associativity means grouping updates differently does not change the result, which matters when branches complete in batches.

## Your task

Diagnose reducer findings from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "first": {
      "id": "receipt",
      "severity": 1
    },
    "second": {
      "id": "receipt",
      "severity": 3
    }
  },
  {
    "first": {
      "id": "receipt",
      "severity": 1
    },
    "second": {
      "id": "estimate",
      "severity": 2
    }
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "A merge must preserve evidence from earlier updates."
- "Return new evidence only; the reducer already has previous values."
- "Severity must not decrease when a later finding is weaker."
- "Canonical presentation must not depend on arrival order."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-10
uv run gym check 02-10
uv run gym hint 02-10
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
