# B1-16 — Diagnose typescript agents from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

The TypeScript model factory returns a scripted LangChain fake with tool calls. A manual StateGraph loop and createAgent consume the same trajectory, making their roles and call identities directly comparable. The Python gym bridge executes the selected TypeScript file in Node; it never supplies the business answer itself.

## Your task

Diagnose typescript agents from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

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
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Return the tool result to the manual agent before ending."
- "Respect the configured loop budget in both JavaScript agents."
- "Preserve the expected tool-call identity across the language port."
- "Register the same evidence tool in the prebuilt implementation."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start B1-16
uv run gym check B1-16
uv run gym hint B1-16
```

## Reading

[Module lesson](../../../../modules/bonus/B1_langgraph_js/README.md) · [Official guide](https://docs.langchain.com/oss/javascript/langchain/agents)
