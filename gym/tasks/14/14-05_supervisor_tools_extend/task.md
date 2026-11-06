# 14-05 — Extend supervisor tools: Give the policy specialist authoritative scoped evidence.

Type: extend. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

A supervisor may call specialists as tools. Each specialist gets a narrow evidence prompt and a private message history; the supervisor receives only the returned conclusion. This direct create_agent pattern avoids an extra helper package. More agents add calls and failure boundaries, so compare them against a single-agent baseline.

## Your task

Give the policy specialist authoritative scoped evidence. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "question": "Review policy and fraud evidence.",
    "private_note": "Synthetic phone: 555-0100"
  },
  {
    "question": "Which document is missing?",
    "private_note": "Synthetic address withheld"
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 14-05
uv run gym check 14-05
uv run gym hint 14-05
```

## Reading

[Module lesson](../../../../modules/14_multi_agent_systems/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/multi-agent/subagents)
