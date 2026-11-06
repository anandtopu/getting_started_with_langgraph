# 14-07 — Build handoffs: Address the parent graph when handing off to its specialist.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

Command.PARENT transfers control from a child graph to a node in its parent. The shared messages channel uses add_messages. A tool-based handoff includes both the AI request and its ToolMessage acknowledgment so the next specialist receives a valid conversation. Parent destinations must not be declared as local child nodes.

## Your task

Address the parent graph when handing off to its specialist. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

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

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 14-07
uv run gym check 14-07
uv run gym hint 14-07
```

## Reading

[Module lesson](../../../../modules/14_multi_agent_systems/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/multi-agent/handoffs)
