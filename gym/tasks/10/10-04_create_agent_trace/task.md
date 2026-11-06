# 10-04 — Diagnose create agent from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

create_agent builds a standard model/tool loop on LangGraph. Start there for ordinary tool use; use a custom StateGraph when the business process requires explicit gates or branches. The compiled agent still accepts state, can be inspected as a graph, and emits normal messages.

## Your task

Diagnose create agent from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "policy_id": "POL-0001"
  },
  {
    "policy_id": "MISSING"
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Register the requested tool with the prebuilt agent."
- "Reject unknown policy IDs, not the known fixture."
- "Pass through the requested policy instead of silently substituting another."
- "Expose the final agent answer rather than the original question."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 10-04
uv run gym check 10-04
uv run gym hint 10-04
```

## Reading

[Module lesson](../../../../modules/10_prebuilt_agents/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/agents)
