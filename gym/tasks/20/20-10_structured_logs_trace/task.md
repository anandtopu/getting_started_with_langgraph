# 20-10 — Trace structured logs: Attach each log record to its actual node.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Structured logs are small machine-readable records correlated by thread and run. An allowlist excludes raw prompts, contact details, and credentials rather than hoping a redactor recognizes every secret. Random run identifiers belong in operational logs but should be normalized out of teaching snapshots.

## Your task

Attach each log record to its actual node. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 20-10
uv run gym check 20-10
uv run gym hint 20-10
```

## Reading

[Module lesson](../../../../modules/20_observability_and_debugging/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/pregel)
