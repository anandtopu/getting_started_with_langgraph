# 02-10 — Trace reducer findings: Return new evidence only; the reducer already has previous values.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A channel is one state field together with its update rule. The default rule overwrites. An Annotated reducer combines the old and new values. Associativity means grouping updates differently does not change the result, which matters when branches complete in batches.

## Your task

Return new evidence only; the reducer already has previous values. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-10
uv run gym check 02-10
uv run gym hint 02-10
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
