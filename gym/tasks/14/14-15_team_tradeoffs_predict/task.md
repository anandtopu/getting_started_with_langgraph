# 14-15 — Predict team tradeoffs across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

A swarm-style team routes according to the active specialist, without requiring a central supervisor on every transition. Its business budget is distinct from the graph recursion limit. This controlled four-role comparison measures calls and completion; scripted answers do not establish that the team is smarter than the one-call baseline.

## Your task

Predict team tradeoffs across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "budget": 4,
    "start_agent": "intake"
  },
  {
    "budget": 2,
    "start_agent": "intake"
  },
  {
    "budget": 0,
    "start_agent": "intake"
  },
  {
    "budget": 4,
    "start_agent": "fraud"
  },
  {
    "budget": -1,
    "start_agent": "intake"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 14-15
uv run gym check 14-15
uv run gym hint 14-15
```

## Reading

[Module lesson](../../../../modules/14_multi_agent_systems/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/multi-agent)
