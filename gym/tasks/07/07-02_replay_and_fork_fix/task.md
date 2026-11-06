# 07-02 — Fix replay and fork: Replay the new fork configuration, not its uncorrected parent.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

A checkpoint configuration identifies a historical state. Replaying it reruns later work; it does not merely print an old answer. update_state with as_node forks from that checkpoint and schedules its successors. Approval encountered again is requested again.

## Your task

Replay the new fork configuration, not its uncorrected parent. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 07-02
uv run gym check 07-02
uv run gym hint 07-02
```

## Reading

[Module lesson](../../../../modules/07_time_travel_and_streaming/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/use-time-travel)
