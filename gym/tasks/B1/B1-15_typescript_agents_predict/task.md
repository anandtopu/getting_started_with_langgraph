# B1-15 — Predict typescript agents across the declared cases

Type: predict. Difficulty: easy. No live model, key, or network is required.

## The claim scenario

The TypeScript model factory returns a scripted LangChain fake with tool calls. A manual StateGraph loop and createAgent consume the same trajectory, making their roles and call identities directly comparable. The Python gym bridge executes the selected TypeScript file in Node; it never supplies the business answer itself.

## Your task

Predict typescript agents across the declared cases Predict each result before running the example. Keep the observations in the listed input order.

## Inputs and acceptance

```json
[
  {
    "policy_id": "POL-0001",
    "recursion_limit": 12
  },
  {
    "policy_id": "POL-0001",
    "recursion_limit": 1
  },
  {
    "policy_id": "MISSING",
    "recursion_limit": 12
  }
]
```

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B1-15
uv run gym check B1-15
uv run gym hint B1-15
```

## Reading

[Module lesson](../../../../modules/bonus/B1_langgraph_js/README.md) · [Official guide](https://docs.langchain.com/oss/javascript/langchain/agents)
