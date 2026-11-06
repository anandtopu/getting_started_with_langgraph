# 12-02 — Fix chains and gates: Stop the chain when the fact gate fails.

Type: fix. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Prompt chaining fixes the order of model operations. A deterministic gate compares extracted facts with the authoritative policy before allowing a draft. The validated category can route work, but a model cannot override the gate. A blocked extraction should not consume a drafting call.

## Your task

Stop the chain when the fact gate fails. Preserve run(case) and the existing public functions. Return a JSON-compatible result. Do not import the reference solution or hard-code one fixture.

## Inputs and acceptance

```json
[
  {
    "category": "policy",
    "policy_deductible": 100000,
    "extracted_deductible": 100000
  },
  {
    "category": "documents",
    "policy_deductible": 100000,
    "extracted_deductible": 100000
  },
  {
    "category": "policy",
    "policy_deductible": 100000,
    "extracted_deductible": 90000
  },
  {
    "category": "approve",
    "policy_deductible": 100000,
    "extracted_deductible": 100000
  },
  {
    "category": "policy",
    "policy_deductible": 100000,
    "extracted_deductible": true
  }
]
```

cases.json declares the expected output or expected exception type for every input. Exceptions are observed by the grader; import errors are setup failures. The starter's demo prints a known runtime error when appropriate, so you can inspect it without losing the exercise context.

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-02
uv run gym check 12-02
uv run gym hint 12-02
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
