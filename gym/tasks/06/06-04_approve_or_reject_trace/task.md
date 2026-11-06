# 06-04 — Trace approve or reject: An interrupt needs persistence to resume the saved task.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

interrupt pauses graph work and returns a request to the caller. A checkpointer and stable thread preserve that pause. Command(resume=...) supplies the response; the interrupted node restarts, so validate the response rather than trusting its shape.

## Your task

An interrupt needs persistence to resume the saved task. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "amount_cents": 600000,
    "decision": {
      "approved": true
    }
  },
  {
    "amount_cents": 600000,
    "decision": {
      "approved": false
    }
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-04
uv run gym check 06-04
uv run gym hint 06-04
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
