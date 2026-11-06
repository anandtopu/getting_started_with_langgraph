# 02-17 — Extend state boundaries: Customer-facing correction must normalize text.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Input and output schemas define an API boundary; private channels can still exist inside the graph. Messages are records with roles, text, and IDs. add_messages appends new IDs and replaces an existing ID, so correcting one message need not duplicate it.

## Your task

Append a customer-safe explanation without exposing internal notes or duplicating the original message. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 02-17
uv run gym check 02-17
uv run gym hint 02-17
```

## Reading

[Module lesson](../../../../modules/02_state_and_reducers/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-state)
