# 06-16 — Trace safe reentry: Effects before interrupt repeat when the node restarts.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

On resume, Python starts the interrupted node again. Code before interrupt can therefore repeat. Move effects after validated approval into separate checkpointed work, and use a stable idempotency key because a crash can occur after a write but before its checkpoint.

## Your task

Effects before interrupt repeat when the node restarts. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "approved": true
  },
  {
    "claim_id": "CLM-0001",
    "approved": false
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-16
uv run gym check 06-16
uv run gym hint 06-16
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
