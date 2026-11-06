# 04-10 — Trace fan out fan in: Parallel writes to an overwrite channel conflict.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Send creates one worker invocation per item with its own input. Parallel workers need a reducer when they write the same channel. defer waits for pending work, which matters when one branch takes more steps than another.

## Your task

Parallel writes to an overwrite channel conflict. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 04-10
uv run gym check 04-10
uv run gym hint 04-10
```

## Reading

[Module lesson](../../../../modules/04_loops_parallel_map_reduce/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/graph-api-send-command)
