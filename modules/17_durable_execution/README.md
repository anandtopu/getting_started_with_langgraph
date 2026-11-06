# 17 — Durable execution and long-running workflows

> After this module you can wait for a contractor estimate and recover after a simulated crash.

**Time:** 120 minutes · **Level:** Advanced · **LLM needed:** No live model · **Cost:** $0 with the included fakes.

**Larkspur Claims Copilot v08** · Practice takes additional time.

## Prerequisites

Complete [External systems and MCP](../16_external_systems_and_mcp/README.md). Read dictionary keys, functions, and Python type hints comfortably. Run uv sync from the repository root.

Optional installation requirements are listed in [the setup guide](../../docs/OPTIONAL_DEPENDENCIES.md). Use `uv run --no-sync` after installing extras so subsequent commands retain that environment.

## Learning objectives

- Implement and explain Durability modes in failures; task-wrapped side effects; checkpointed nondeterminism; idempotency; crash windows.
- Implement and explain RetryPolicy after transient failures; async node timeouts; TimeoutPolicy; NodeError and error_handler; compensation; RunControl graceful drain.
- Implement and explain Durable interrupt waits; simulated time; PostgresSaver and AsyncPostgresSaver; setup lifecycle; shared database persistence.

## The big idea

Wait for a contractor estimate and recover after a simulated crash. Predict the state before running code, then compare the observed result. A state is the data visible to a node; a node is one unit of work; an edge selects later work. A checkpoint is a saved state boundary, not a promise that an external effect happened exactly once.

## How it works

### Durable Side Effects

A task result is reusable only after it is checkpointed. This example kills an owned child after the effect ledger commits but before the task returns, then starts a new process. A payload-bound idempotency key prevents duplicate effects even in that gap. sync, async, and exit durability offer different checkpoint guarantees; none makes an external system transactional with the graph.

A stamped payment register prevents a duplicate even when the worker disappears before filing the receipt.

### Recovery Policies

RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.

Try a temporarily closed service desk twice, then send the claim to review; at closing time finish the current stamped page before shelving it.

### Long Wait Postgres

An interrupt persists a wait without holding a worker open. The simulated receipt date advances three days while the program itself finishes immediately. Reopening the SQLite saver proves connection-lifetime independence. The same graph includes synchronous and asynchronous Postgres variants; schema setup belongs in startup or migrations, not each request.

Put the claim on a dated waiting shelf and let another shift resume it when the estimate arrives.

## Key APIs at a glance

| API / executable example | What it does | When to use it |
| --- | --- | --- |
| SqliteSaver, entrypoint, task — [01_durable_side_effects.py](examples/01_durable_side_effects.py) | Durability modes in failures; task-wrapped side effects; checkpointed nondeterminism; idempotency; crash windows | A task result is reusable only after it is checkpointed. |
| InMemorySaver, GraphDrained, NodeError, StateGraph — [02_recovery_policies.py](examples/02_recovery_policies.py) | RetryPolicy after transient failures; async node timeouts; TimeoutPolicy; NodeError and error_handler; compensation; RunControl graceful drain | RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. |
| SqliteSaver, StateGraph, Command, interrupt — [03_long_wait_postgres.py](examples/03_long_wait_postgres.py) | Durable interrupt waits; simulated time; PostgresSaver and AsyncPostgresSaver; setup lifecycle; shared database persistence | An interrupt persists a wait without holding a worker open. |

## Walkthrough

Run commands from the repository root; the same commands work in PowerShell, macOS, and Linux. Open the source alongside the output. Find the state declaration, node functions, graph connections, and invocation. For a failure, start with the earliest changed field or scheduled node.

```text
uv run python modules/17_durable_execution/examples/01_durable_side_effects.py
```

**Predict, then run:** for {"claim_id": "CLM-0001", "durability": "sync"}, write the resulting fields and any expected error. Then test the boundary cases in tests/durable_side_effects.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "crash_exit": 42,
    "effect_count": 1,
    "claim_id": "CLM-0001",
    "durability": "sync"
  }
}
```

A task result is reusable only after it is checkpointed. This example kills an owned child after the effect ledger commits but before the task returns, then starts a new process. A payload-bound idempotency key prevents duplicate effects even in that gap. sync, async, and exit durability offer different checkpoint guarantees; none makes an external system transactional with the graph.

</details>

```text
uv run python modules/17_durable_execution/examples/02_recovery_policies.py
```

**Predict, then run:** for {"failures": 1, "timeout": false, "drain": true}, write the resulting fields and any expected error. Then test the boundary cases in tests/recovery_policies.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "status": "estimate_received",
    "finished": true,
    "attempts": 2,
    "drained": true
  }
}
```

RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.

</details>

```text
uv run python modules/17_durable_execution/examples/03_long_wait_postgres.py
```

**Predict, then run:** for {"claim_id": "CLM-0001", "received_on": "2026-01-04", "document_id": "DOC-001"}, write the resulting fields and any expected error. Then test the boundary cases in tests/long_wait_postgres.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "interrupts": 1,
    "claim_id": "CLM-0001",
    "requested_on": "2026-01-01",
    "received_on": "2026-01-04",
    "document_id": "DOC-001",
    "waited_days": 3
  }
}
```

An interrupt persists a wait without holding a worker open. The simulated receipt date advances three days while the program itself finishes immediately. Reopening the SQLite saver proves connection-lifetime independence. The same graph includes synchronous and asynchronous Postgres variants; schema setup belongs in startup or migrations, not each request.

</details>

When build_graph needs no arguments, its generated Mermaid diagram is saved beside the example. A diagram records possible edges; a runtime stream records executed work. A single sequence advances one node per superstep. Parallel nodes see the same previous boundary, so they cannot read a sibling's unfinished update.

## When to use it, and when not to

Use these contracts when the claim needs the state or control-flow behavior described above. Keep pure arithmetic and validation in ordinary functions that can be tested independently. A graph, checkpoint, or extra agent adds operational choices; justify it with a concrete failure, pause, branch, or reuse requirement.

## Real-world use case

Wait for a contractor estimate and recover after a simulated crash. The executable milestone uses only fictional records and the shared v08 implementation. [Read the use case](use_case/claims_copilot.py).

```text
uv run python modules/17_durable_execution/use_case/claims_copilot.py
```

Sample output from the synthetic default case:

```json
{
  "waited_days": 3,
  "approved": false,
  "documents": [
    "DOC-001",
    "DOC-ESTIMATE"
  ]
}
```

A real team would connect this boundary to validated records and authenticated roles, then retain the same rejection, ownership, and recovery checks.

## Common bugs

| Symptom or broken contract | Cause and repair | Practice |
| --- | --- | --- |
| Observed `{"value": {"crash_exit": 42, "effect_count": 2, "claim_id": "CLM-0001", "durability": "sync"}}`. Keep the effect identity stable across process death. | Restore `key = "estimate:" + claim_id` and check the boundary cases. | [17-01](../../gym/tasks/17/17-01_durable_side_effects_build/task.md) |
| Observed `{"error": "RuntimeError"}`. Make the crash supervisor recognize the documented owned-worker exit. | Restore `os._exit(42)` and check the boundary cases. | [17-02](../../gym/tasks/17/17-02_durable_side_effects_fix/task.md) |
| Observed `{"value": {"status": "manual_review", "error_type": "ConnectionError", "finished": true, "attempts": 1, "drained": false}}`. Retry the recoverable first failure before routing to manual review. | Restore `max_attempts=2` and check the boundary cases. | [17-07](../../gym/tasks/17/17-07_recovery_policies_build/task.md) |
| Observed `{"value": {"status": "estimate_received", "finished": true, "attempts": 2, "drained": true}}`. Do not label an exhausted or timed-out request as successful. | Restore `"status": "manual_review"` and check the boundary cases. | [17-08](../../gym/tasks/17/17-08_recovery_policies_fix/task.md) |
| Observed `{"value": {"interrupts": 1, "claim_id": "CLM-0001", "requested_on": "2026-01-01", "received_on": "2026-01-04", "document_id": "DOC-001", "waited_days": 3}}`. Reject a receipt date earlier than the request date. | Restore `if elapsed < 0:` and check the boundary cases. | [17-13](../../gym/tasks/17/17-13_long_wait_postgres_build/task.md) |
| Observed `{"value": {"interrupts": 1, "claim_id": "CLM-0001", "requested_on": "2026-01-01", "received_on": "2026-01-04", "document_id": "DOC-001", "waited_days": 0}}`. Compute elapsed business time from explicit dates. | Restore `"waited_days": elapsed` and check the boundary cases. | [17-14](../../gym/tasks/17/17-14_long_wait_postgres_fix/task.md) |

## Practice

- [17-01 — build, easy](../../gym/tasks/17/17-01_durable_side_effects_build/task.md): Build durable side effects: Keep the effect identity stable across process death.
- [17-02 — fix, medium](../../gym/tasks/17/17-02_durable_side_effects_fix/task.md): Fix durable side effects: Make the crash supervisor recognize the documented owned-worker exit.
- [17-03 — predict, easy](../../gym/tasks/17/17-03_durable_side_effects_predict/task.md): Predict durable side effects across the declared cases
- [17-04 — trace, medium](../../gym/tasks/17/17-04_durable_side_effects_trace/task.md): Trace durable side effects: Make the crash supervisor recognize the documented owned-worker exit.
- [17-05 — extend, hard](../../gym/tasks/17/17-05_durable_side_effects_extend/task.md): Extend durable side effects: Recover the original claim identity after restart.
- [17-06 — refactor, hard](../../gym/tasks/17/17-06_durable_side_effects_refactor/task.md): Refactor durable side effects: Report the durable ledger count, not an inferred execution count.
- [17-07 — build, easy](../../gym/tasks/17/17-07_recovery_policies_build/task.md): Build recovery policies: Retry the recoverable first failure before routing to manual review.
- [17-08 — fix, medium](../../gym/tasks/17/17-08_recovery_policies_fix/task.md): Fix recovery policies: Do not label an exhausted or timed-out request as successful.
- [17-09 — predict, easy](../../gym/tasks/17/17-09_recovery_policies_predict/task.md): Predict recovery policies across the declared cases
- [17-10 — trace, medium](../../gym/tasks/17/17-10_recovery_policies_trace/task.md): Trace recovery policies: Do not label an exhausted or timed-out request as successful.
- [17-11 — extend, hard](../../gym/tasks/17/17-11_recovery_policies_extend/task.md): Extend recovery policies: Honor the cooperative shutdown request at the next boundary.
- [17-12 — design, hard](../../gym/tasks/17/17-12_recovery_policies_design/task.md): Design recovery policies and justify the boundary policies
- [17-13 — build, easy](../../gym/tasks/17/17-13_long_wait_postgres_build/task.md): Build long wait postgres: Reject a receipt date earlier than the request date.
- [17-14 — fix, medium](../../gym/tasks/17/17-14_long_wait_postgres_fix/task.md): Fix long wait postgres: Compute elapsed business time from explicit dates.
- [17-15 — predict, easy](../../gym/tasks/17/17-15_long_wait_postgres_predict/task.md): Predict long wait postgres across the declared cases
- [17-16 — trace, medium](../../gym/tasks/17/17-16_long_wait_postgres_trace/task.md): Trace long wait postgres: Compute elapsed business time from explicit dates.
- [17-17 — extend, hard](../../gym/tasks/17/17-17_long_wait_postgres_extend/task.md): Extend long wait postgres: Require the missing document before ending the durable wait.
- [17-18 — refactor, hard](../../gym/tasks/17/17-18_long_wait_postgres_refactor/task.md): Refactor long wait postgres: Preserve the received evidence identifier on resume.

Start with tasks 01, 02, 09, 10, 17, and 18 in this module. Finish the other tasks for full practice. Hints are progressive; solution exposure is recorded. Predict and Trace tasks use answer JSON, not a code starter.

## Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_durable_side_effects.py using one claim from its input cases.
2. Diagnose this broken behavior: Make the crash supervisor recognize the documented owned-worker exit. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_recovery_policies.py using one claim from its input cases.
4. Diagnose this broken behavior: Do not label an exhausted or timed-out request as successful. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_long_wait_postgres.py using one claim from its input cases.
6. Diagnose this broken behavior: Compute elapsed business time from explicit dates. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. A task result is reusable only after it is checkpointed. This example kills an owned child after the effect ledger commits but before the task returns, then starts a new process. A payload-bound idempotency key prevents duplicate effects even in that gap. sync, async, and exit durability offer different checkpoint guarantees; none makes an external system transactional with the graph.
2. Make the crash supervisor recognize the documented owned-worker exit. Compare the normal case with the boundary fixtures and identify the first differing update.
3. RetryPolicy repeats selected transient failures; TimeoutPolicy bounds asynchronous attempts. After retries are exhausted, a NodeError-aware handler routes to manual review. RunControl requests a cooperative drain after the current superstep, preserving a resumable boundary rather than killing in-flight work. Recovery must not invent a successful external effect.
4. Do not label an exhausted or timed-out request as successful. Compare the normal case with the boundary fixtures and identify the first differing update.
5. An interrupt persists a wait without holding a worker open. The simulated receipt date advances three days while the program itself finishes immediately. Reopening the SQLite saver proves connection-lifetime independence. The same graph includes synchronous and asynchronous Postgres variants; schema setup belongs in startup or migrations, not each request.
6. Compute elapsed business time from explicit dates. Compare the normal case with the boundary fixtures and identify the first differing update.

</details>

## Cost and safety

The default commands cost $0: deterministic Python and, in model lessons, scripted local fakes. They consume no hosted tokens and make no real payments or emails. Optional live experiments use the provider configured in .env; a short one-to-four-call exercise is usually cents, but verify your provider's current token prices and set a budget. Ollama can run locally without a hosted bill. Temporary checkpoint files are isolated from the committed dataset. Keep real customer details and credentials out of graph state.

## Key takeaways

- State visibility and update rules determine what a node can safely assume.
- Check normal, missing, boundary, and failure cases before trusting a workflow.
- Separate observed execution from diagrams, predictions, and durable history.
- Model output is evidence to validate, never an authorization grant.
- A saved checkpoint and an external effect have separate durability boundaries.

## Go deeper

- [durable side effects official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
- [recovery policies official guide](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)
- [long wait postgres official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)

## Next:

Continue to [module 18: Streaming to user interfaces](../../modules/18_streaming_user_interfaces/README.md).
