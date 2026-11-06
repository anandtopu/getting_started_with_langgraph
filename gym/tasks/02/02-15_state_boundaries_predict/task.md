# 02-15 — Predict state boundaries across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Input and output schemas define an API boundary; private channels can still exist inside the graph. Messages are records with roles, text, and IDs. add_messages appends new IDs and replaces an existing ID, so correcting one message need not duplicate it.

## Your task

Predict state boundaries across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "text": "  Pipe burst  "
  },
  {
    "claim_id": "CLM-0022",
    "text": " theft "
  },
  {
    "claim_id": "CLM-0001",
    "text": " ",
    "private_notes": "Untrusted supplied note"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-15
uv run gym check 02-15
uv run gym hint 02-15
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
