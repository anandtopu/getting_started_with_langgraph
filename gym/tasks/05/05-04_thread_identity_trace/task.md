# 05-04 — Diagnose thread identity from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A checkpointer saves graph state under a thread ID. New input on that thread starts another run against its saved state. Resuming a pending operation is different: use the saved continuation or an interrupt response rather than pretending it is a new claim.

## Your task

Diagnose thread identity from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "first_id": "CLM-0001",
    "second_id": "CLM-0002"
  },
  {
    "first_id": "CLM-A",
    "second_id": "CLM-B"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Saved notes must survive a second invocation on the same graph."
- "A persisted invocation needs an explicit thread identifier."
- "Claim identity must participate in the thread mapping."
- "Continuing a session must not discard earlier notes."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 05-04
uv run gym check 05-04
uv run gym hint 05-04
```

## Reading

[Module lesson](../../../../modules/05_persistence_and_threads/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
