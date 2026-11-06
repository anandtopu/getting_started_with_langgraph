# 12-13 — Build evaluator optimizer: Stop unsuccessful revision at the configured budget.

Type: build. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

The evaluator names concrete factual and tone defects; the optimizer receives that feedback before another draft. Stop on success or a strict attempt budget. A deterministic substring check is deliberately limited: it teaches loop control and must not be mistaken for a production factuality evaluator.

## Your task

Stop unsuccessful revision at the configured budget. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "drafts": [
      "Your deductible is 90000 cents.",
      "Thank you. Your deductible is 100000 cents."
    ],
    "budget": 3
  },
  {
    "drafts": [
      "Your deductible is 90000 cents.",
      "Thank you. Your deductible is 100000 cents."
    ],
    "budget": 1
  },
  {
    "drafts": [
      "Wrong amount."
    ],
    "budget": 2
  },
  {
    "drafts": [
      "Thank you. Your deductible is 100000 cents."
    ],
    "budget": 3
  },
  {
    "drafts": [
      "Your deductible is 90000 cents.",
      "Thank you. Your deductible is 100000 cents."
    ],
    "budget": 0
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-13
uv run gym check 12-13
uv run gym hint 12-13
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
