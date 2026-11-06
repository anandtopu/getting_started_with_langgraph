# 09-16 — Diagnose tool runtime from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

ToolRuntime injects trusted context, graph state, the Store, and tool_call_id without exposing them as model-selectable fields. A tool returning Command can update graph state and acknowledge its own request. Customer identity belongs in authenticated context, not in an argument the model invents.

## Your task

Diagnose tool runtime from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "customer_id": "CUS-0001",
    "preference": "email"
  },
  {
    "customer_id": "CUS-0020",
    "preference": "sms"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Write only in the trusted customer namespace."
- "Keep the graph state consistent with the Store write."
- "Support the declared SMS contact preference."
- "Acknowledge the tool request using its injected identity."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 09-16
uv run gym check 09-16
uv run gym hint 09-16
```

## Reading

[Module lesson](../../../../modules/09_tools_and_agent_loop/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/tools)
