# 05-10 — Diagnose sqlite lifetime from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Memory persistence ends with its process. A SQLite saver stores checkpoints on disk and must remain open for every invocation that uses it. Explicit context managers release connections, including on Windows where open files can prevent cleanup.

## Your task

Diagnose sqlite lifetime from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001"
  },
  {
    "claim_id": "CLM-0199"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "A restarted process must merge the new note with stored notes."
- "A compiled graph cannot use a saver whose connection has closed."
- "Both processes must reopen the same logical claim thread."
- "Resource-lifetime refactoring must preserve continuation input."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-10
uv run gym check 05-10
uv run gym hint 05-10
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
