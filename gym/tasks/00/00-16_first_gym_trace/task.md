# 00-16 — Trace first gym: Labels need case normalization before comparison.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

An assertion compares an observed result with an explicit requirement. A failing starter is useful when it runs and shows a wrong business result. Hints guide a repair; viewing a solution is recorded separately from independent work.

## Your task

Labels need case normalization before comparison. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_type": " Water ",
    "claim_id": "CLM-0001"
  },
  {
    "claim_type": "THEFT",
    "claim_id": "CLM-0001"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 00-16
uv run gym check 00-16
uv run gym hint 00-16
```

## Reading

[Module lesson](../../../../modules/00_setup/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/test)
