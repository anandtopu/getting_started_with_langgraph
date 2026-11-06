# 04-12 — Refactor fan out fan in: Do not treat arrival order as the public result order.

Type: refactor. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Send creates one worker invocation per item with its own input. Parallel workers need a reducer when they write the same channel. defer waits for pending work, which matters when one branch takes more steps than another.

## Your task

Do not treat arrival order as the public result order. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "documents": [
      {
        "id": "DOC-001",
        "kind": "estimate"
      },
      {
        "id": "DOC-021",
        "kind": "police"
      }
    ]
  },
  {
    "documents": []
  },
  {
    "documents": [
      {
        "id": "DOC-Z",
        "kind": "estimate"
      }
    ]
  },
  {
    "documents": [
      {
        "id": "DOC-Z",
        "kind": "police"
      },
      {
        "id": "DOC-A",
        "kind": "receipt"
      },
      {
        "id": "DOC-B",
        "kind": "police"
      }
    ]
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-12
uv run gym check 04-12
uv run gym hint 04-12
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command)
