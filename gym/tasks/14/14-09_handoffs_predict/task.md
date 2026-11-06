# 14-09 — Predict handoffs across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Command.PARENT transfers control from a child graph to a node in its parent. The shared messages channel uses add_messages. A tool-based handoff includes both the AI request and its ToolMessage acknowledgment so the next specialist receives a valid conversation. Parent destinations must not be declared as local child nodes.

## Your task

Predict handoffs across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "claim_id": "CLM-0001",
    "question": "Explain the deductible."
  },
  {
    "claim_id": "CLM-0400",
    "question": "What is the water deductible?"
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 14-09
uv run gym check 14-09
uv run gym hint 14-09
```

## Reading

[Module lesson](../../../../modules/14_multi_agent_systems/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs)
