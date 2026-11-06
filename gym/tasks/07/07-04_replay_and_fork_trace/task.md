# 07-04 — Diagnose replay and fork from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A checkpoint configuration identifies a historical state. Replaying it reruns later work; it does not merely print an old answer. update_state with as_node forks from that checkpoint and schedules its successors. Approval encountered again is requested again.

## Your task

Diagnose replay and fork from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "amount_cents": 100000,
    "corrected_amount": 600000
  },
  {
    "amount_cents": 200000,
    "corrected_amount": 50000
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "A fork must contain the corrected evidence."
- "Replay the new fork configuration, not its uncorrected parent."
- "Parentage must identify the selected historical evidence."
- "Replaying a completed checkpoint is different from rerunning pending review."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 07-04
uv run gym check 07-04
uv run gym hint 07-04
```

## Reading

[Module lesson](../../../../modules/07_time_travel_and_streaming/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
