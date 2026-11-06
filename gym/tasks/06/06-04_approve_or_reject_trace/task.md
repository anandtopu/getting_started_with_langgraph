# 06-04 — Diagnose approve or reject from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

interrupt pauses graph work and returns a request to the caller. A checkpointer and stable thread preserve that pause. Command(resume=...) supplies the response; the interrupted node restarts, so validate the response rather than trusting its shape.

## Your task

Diagnose approve or reject from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

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

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "A rejected proposal must not become an approved result."
- "An interrupt needs persistence to resume the saved task."
- "Only a validated boolean authorizes this synthetic decision."
- "Replacing a callback must preserve the actual human response."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 06-04
uv run gym check 06-04
uv run gym hint 06-04
```

## Reading

[Module lesson](../../../../modules/06_human_in_the_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
