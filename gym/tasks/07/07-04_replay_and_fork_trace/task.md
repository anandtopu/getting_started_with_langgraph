# 07-04 — Trace replay and fork: Replay the new fork configuration, not its uncorrected parent.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A checkpoint configuration identifies a historical state. Replaying it reruns later work; it does not merely print an old answer. update_state with as_node forks from that checkpoint and schedules its successors. Approval encountered again is requested again.

## Your task

Replay the new fork configuration, not its uncorrected parent. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 07-04
uv run gym check 07-04
uv run gym hint 07-04
```

## Reading

[Module lesson](../../../../modules/07_time_travel_and_streaming/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
