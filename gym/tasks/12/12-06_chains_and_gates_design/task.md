# 12-06 — Design chains and gates and justify the boundary policies

Type: design. Difficulty: hard. No live model, key, or network is required.

## The claim scenario

Prompt chaining fixes the order of model operations. A deterministic gate compares extracted facts with the authoritative policy before allowing a draft. The validated category can route work, but a model cannot override the gate. A blocked extraction should not consume a drafting call.

## Your task

Design chains and gates and justify the boundary policies Implement the choices in run and complete design.md using the rubric.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 12-06
uv run gym check 12-06
uv run gym hint 12-06
```

## Reading

[Module lesson](../../../../modules/12_workflow_patterns/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
