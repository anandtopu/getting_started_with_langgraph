# 20-10 — Diagnose structured logs from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Structured logs are small machine-readable records correlated by thread and run. An allowlist excludes raw prompts, contact details, and credentials rather than hoping a redactor recognizes every secret. Random run identifiers belong in operational logs but should be normalized out of teaching snapshots.

## Your task

Diagnose structured logs from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "thread_id": "claim-thread",
    "run_id": "review-1",
    "description": "Synthetic contact: 555-0100",
    "api_key": "synthetic-secret"
  },
  {
    "thread_id": "second-claim",
    "run_id": "review-2",
    "description": "Synthetic contact: 555-0100",
    "api_key": "synthetic-secret"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Use the documented event category for node completion."
- "Attach each log record to its actual node."
- "Retain the caller's thread correlation identifier."
- "Do not report a successful node as failed during logging refactors."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-10
uv run gym check 20-10
uv run gym hint 20-10
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/pregel)
