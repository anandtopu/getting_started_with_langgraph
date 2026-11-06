# 17-10 — Diagnose recovery policies from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.

## Your task

Diagnose recovery policies from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses, parent-graph handoffs, and cancellation are labeled separately from execution failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "failures": 1,
    "timeout": false,
    "drain": true
  },
  {
    "failures": 3,
    "timeout": false,
    "drain": true
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Retry the recoverable first failure before routing to manual review."
- "Do not label an exhausted or timed-out request as successful."
- "Honor the cooperative shutdown request at the next boundary."
- "Finish the recovery path after success or error handling."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 17-10
uv run gym check 17-10
uv run gym hint 17-10
```

## Reading

[Module lesson](../../../../modules/17_durable_execution/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
