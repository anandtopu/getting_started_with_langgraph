# 21 — Security and guardrails

> After this module you can keep injected claim text from authorizing payouts or crossing customer boundaries.

**Time:** 150 minutes · **Level:** Advanced · **LLM needed:** No live model · **Cost:** $0 with the included fakes.

**Larkspur Claims Copilot v10** · Practice takes additional time.

## Prerequisites

Complete [Observability and visual debugging](../20_observability_and_debugging/README.md). Read dictionary keys, functions, and Python type hints comfortably. Run uv sync from the repository root.

Optional installation requirements are listed in [the setup guide](../../docs/OPTIONAL_DEPENDENCIES.md). Use `uv run --no-sync` after installing extras so subsequent commands retain that environment.

## Learning objectives

- Implement and explain Prompt injection; deterministic authorization; validated structured output; allowlisted routes; least-privilege tools.
- Implement and explain Approval before side effects; authorization outside the model; recursion and tool-call budgets; token/cost budgets; audit events.
- Implement and explain PII minimization; EncryptedSerializer; encryption key handling; retention and deletion; audit-trail limitations.

## The big idea

Keep injected claim text from authorizing payouts or crossing customer boundaries. Predict the state before running code, then compare the observed result. A state is the data visible to a node; a node is one unit of work; an edge selects later work. A checkpoint is a saved state boundary, not a promise that an external effect happened exactly once.

## How it works

### Untrusted Input

Claim text and retrieved documents are untrusted data. A structured schema rejects extra authority fields and impossible amounts, while deterministic rules select routes. Neither a model's confidence nor a sentence saying 'approved' grants permission. Tool capabilities are independently restricted to the minimum required evidence reads.

A customer's handwritten instruction cannot become an employee access badge.

### Approval And Limits

Admission checks reject a planned operation that exceeds the configured call or estimated-token budget. They supplement, rather than replace, runtime model/tool limits and recursion bounds. The API separately verifies role, current interrupt identity, and confirmed coverage before recording a payload-bound synthetic effect. Token estimates are conservative planning inputs, not a guaranteed hosted bill.

A spending envelope limits the planned work, while an authorized signature is still required for the actual payment.

### Private Checkpoints

EncryptedSerializer encrypts serialized checkpoint payloads using an externally supplied key. The example creates an ephemeral key and never returns it. Minimize PII before storage; encryption does not hide every database field or replace access control, key rotation, and retention. A wrong key fails authentication, and deleting a thread is separate from deleting Store memories and backups.

Lock the retained folder, keep its key outside the folder, and still follow a shredding schedule.

## Key APIs at a glance

| API / executable example | What it does | When to use it |
| --- | --- | --- |
| AIMessage — [01_untrusted_input.py](examples/01_untrusted_input.py) | Prompt injection; deterministic authorization; validated structured output; allowlisted routes; least-privilege tools | Claim text and retrieved documents are untrusted data. |
| run(case) — [02_approval_and_limits.py](examples/02_approval_and_limits.py) | Approval before side effects; authorization outside the model; recursion and tool-call budgets; token/cost budgets; audit events | Admission checks reject a planned operation that exceeds the configured call or estimated-token budget. |
| InMemorySaver, EncryptedSerializer, StateGraph — [03_private_checkpoints.py](examples/03_private_checkpoints.py) | PII minimization; EncryptedSerializer; encryption key handling; retention and deletion; audit-trail limitations | EncryptedSerializer encrypts serialized checkpoint payloads using an externally supplied key. |

## Walkthrough

Run commands from the repository root; the same commands work in PowerShell, macOS, and Linux. Open the source alongside the output. Find the state declaration, node functions, graph connections, and invocation. For a failure, start with the earliest changed field or scheduled node.

```text
uv run python modules/21_security_and_guardrails/examples/01_untrusted_input.py
```

**Predict, then run:** for {"extra_authority": false, "amount_cents": 600000}, write the resulting fields and any expected error. Then test the boundary cases in tests/untrusted_input.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "route": "specialist",
    "payment_authorized": false,
    "model_fields": [
      "amount_cents",
      "claim_type",
      "confidence",
      "loss_date"
    ],
    "tool_permissions": [
      "read_synthetic_policy"
    ]
  }
}
```

Claim text and retrieved documents are untrusted data. A structured schema rejects extra authority fields and impossible amounts, while deterministic rules select routes. Neither a model's confidence nor a sentence saying 'approved' grants permission. Tool capabilities are independently restricted to the minimum required evidence reads.

</details>

```text
uv run python modules/21_security_and_guardrails/examples/02_approval_and_limits.py
```

**Predict, then run:** for {"approved": true, "planned_calls": 10, "call_budget": 12, "estimated_tokens": 1000, "token_budget": 2000}, write the resulting fields and any expected error. Then test the boundary cases in tests/approval_and_limits.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "admitted": true,
    "effects": 1,
    "status": "recorded",
    "customer_approval_status": 403,
    "stale_status": 409
  }
}
```

Admission checks reject a planned operation that exceeds the configured call or estimated-token budget. They supplement, rather than replace, runtime model/tool limits and recursion bounds. The API separately verifies role, current interrupt identity, and confirmed coverage before recording a payload-bound synthetic effect. Token estimates are conservative planning inputs, not a guaranteed hosted bill.

</details>

```text
uv run python modules/21_security_and_guardrails/examples/03_private_checkpoints.py
```

**Predict, then run:** for {"note": "Synthetic customer phone 555-0100", "delete": true, "wrong_key": false}, write the resulting fields and any expected error. Then test the boundary cases in tests/private_checkpoints.json.

<details>
<summary>Reveal the checked result</summary>

```json
{
  "value": {
    "plaintext_visible": false,
    "roundtrip": true,
    "checkpoint_plaintext_visible": false,
    "retained": false,
    "key_logged": false
  }
}
```

EncryptedSerializer encrypts serialized checkpoint payloads using an externally supplied key. The example creates an ephemeral key and never returns it. Minimize PII before storage; encryption does not hide every database field or replace access control, key rotation, and retention. A wrong key fails authentication, and deleting a thread is separate from deleting Store memories and backups.

</details>

When build_graph needs no arguments, its generated Mermaid diagram is saved beside the example. A diagram records possible edges; a runtime stream records executed work. A single sequence advances one node per superstep. Parallel nodes see the same previous boundary, so they cannot read a sibling's unfinished update.

## When to use it, and when not to

Use these contracts when the claim needs the state or control-flow behavior described above. Keep pure arithmetic and validation in ordinary functions that can be tested independently. A graph, checkpoint, or extra agent adds operational choices; justify it with a concrete failure, pause, branch, or reuse requirement.

## Real-world use case

Keep injected claim text from authorizing payouts or crossing customer boundaries. The executable milestone uses only fictional records and the shared v10 implementation. [Read the use case](use_case/claims_copilot.py).

```text
uv run python modules/21_security_and_guardrails/use_case/claims_copilot.py
```

Sample output from the synthetic default case:

```json
{
  "approved": {
    "created": 201,
    "foreign_status": 404,
    "customer_approval_status": 403,
    "stale_status": 409,
    "effects": 1,
    "status": "recorded",
    "progress_events": 2
  },
  "rejected": {
    "created": 201,
    "foreign_status": 404,
    "customer_approval_status": 403,
    "stale_status": 409,
    "effects": 0,
    "status": "not_approved",
    "progress_events": 2
  }
}
```

A real team would connect this boundary to validated records and authenticated roles, then retain the same rejection, ownership, and recovery checks.

## Common bugs

| Symptom or broken contract | Cause and repair | Practice |
| --- | --- | --- |
| Observed `{"value": {"route": "specialist", "payment_authorized": true, "model_fields": ["amount_cents", "claim_type", "confidence", "loss_date"], "tool_permissions": ["read_synthetic_policy"]}}`. Do not let extracted text authorize a payment. | Restore `"payment_authorized": False` and check the boundary cases. | [21-01](../../gym/tasks/21/21-01_untrusted_input_build/task.md) |
| Observed `{"value": {"route": "fast_track", "payment_authorized": false, "model_fields": ["amount_cents", "claim_type", "confidence", "loss_date"], "tool_permissions": ["read_synthetic_policy"]}}`. Preserve validated amounts before applying deterministic routing. | Restore `"amount_cents": case["amount_cents"]` and check the boundary cases. | [21-02](../../gym/tasks/21/21-02_untrusted_input_fix/task.md) |
| Observed `{"value": {"admitted": true, "effects": 1, "status": "recorded", "customer_approval_status": 403, "stale_status": 409}}`. Enforce the separate planned-call budget. | Restore `case["planned_calls"] > case["call_budget"]` and check the boundary cases. | [21-07](../../gym/tasks/21/21-07_approval_and_limits_build/task.md) |
| Observed `{"value": {"admitted": true, "effects": 1, "status": "recorded", "customer_approval_status": 403, "stale_status": 409}}`. Reject an operation above the token admission budget. | Restore `case["estimated_tokens"] > case["token_budget"]` and check the boundary cases. | [21-08](../../gym/tasks/21/21-08_approval_and_limits_fix/task.md) |
| Observed `{"value": {"plaintext_visible": false, "roundtrip": true, "checkpoint_plaintext_visible": true, "retained": false, "key_logged": false}}`. Install encryption on the actual checkpointer, not just a standalone serialization demo. | Restore `InMemorySaver(serde=serializer)` and check the boundary cases. | [21-13](../../gym/tasks/21/21-13_private_checkpoints_build/task.md) |
| Observed `{"value": {"plaintext_visible": false, "roundtrip": true, "checkpoint_plaintext_visible": false, "retained": true, "key_logged": false}}`. Apply the requested thread-retention deletion. | Restore `if case["delete"]:` and check the boundary cases. | [21-14](../../gym/tasks/21/21-14_private_checkpoints_fix/task.md) |

## Practice

- [21-01 — build, easy](../../gym/tasks/21/21-01_untrusted_input_build/task.md): Build untrusted input: Do not let extracted text authorize a payment.
- [21-02 — fix, medium](../../gym/tasks/21/21-02_untrusted_input_fix/task.md): Fix untrusted input: Preserve validated amounts before applying deterministic routing.
- [21-03 — predict, easy](../../gym/tasks/21/21-03_untrusted_input_predict/task.md): Predict untrusted input across the declared cases
- [21-04 — trace, medium](../../gym/tasks/21/21-04_untrusted_input_trace/task.md): Trace untrusted input: Preserve validated amounts before applying deterministic routing.
- [21-05 — extend, hard](../../gym/tasks/21/21-05_untrusted_input_extend/task.md): Extend untrusted input: Expose and reject an unexpected authority field instead of silently hiding it from validation.
- [21-06 — refactor, hard](../../gym/tasks/21/21-06_untrusted_input_refactor/task.md): Refactor untrusted input: Keep model-visible tool capabilities read-only.
- [21-07 — build, easy](../../gym/tasks/21/21-07_approval_and_limits_build/task.md): Build approval and limits: Enforce the separate planned-call budget.
- [21-08 — fix, medium](../../gym/tasks/21/21-08_approval_and_limits_fix/task.md): Fix approval and limits: Reject an operation above the token admission budget.
- [21-09 — predict, easy](../../gym/tasks/21/21-09_approval_and_limits_predict/task.md): Predict approval and limits across the declared cases
- [21-10 — trace, medium](../../gym/tasks/21/21-10_approval_and_limits_trace/task.md): Trace approval and limits: Reject an operation above the token admission budget.
- [21-11 — extend, hard](../../gym/tasks/21/21-11_approval_and_limits_extend/task.md): Extend approval and limits: Keep a human rejection from creating an effect.
- [21-12 — design, hard](../../gym/tasks/21/21-12_approval_and_limits_design/task.md): Design approval and limits and justify the boundary policies
- [21-13 — build, easy](../../gym/tasks/21/21-13_private_checkpoints_build/task.md): Build private checkpoints: Install encryption on the actual checkpointer, not just a standalone serialization demo.
- [21-14 — fix, medium](../../gym/tasks/21/21-14_private_checkpoints_fix/task.md): Fix private checkpoints: Apply the requested thread-retention deletion.
- [21-15 — predict, easy](../../gym/tasks/21/21-15_private_checkpoints_predict/task.md): Predict private checkpoints across the declared cases
- [21-16 — trace, medium](../../gym/tasks/21/21-16_private_checkpoints_trace/task.md): Trace private checkpoints: Apply the requested thread-retention deletion.
- [21-17 — extend, hard](../../gym/tasks/21/21-17_private_checkpoints_extend/task.md): Extend private checkpoints: Verify that a wrong encryption key cannot restore the payload.
- [21-18 — refactor, hard](../../gym/tasks/21/21-18_private_checkpoints_refactor/task.md): Refactor private checkpoints: Check exact restoration after successful authenticated decryption.

Start with tasks 01, 02, 09, 10, 17, and 18 in this module. Finish the other tasks for full practice. Hints are progressive; solution exposure is recorded. Predict and Trace tasks use answer JSON, not a code starter.

## Quiz

Predict first; explain in your own words.

1. Explain the contract in 01_untrusted_input.py using one claim from its input cases.
2. Diagnose this broken behavior: Preserve validated amounts before applying deterministic routing. Which observation distinguishes the repair from a default-case-only fix?
3. Explain the contract in 02_approval_and_limits.py using one claim from its input cases.
4. Diagnose this broken behavior: Reject an operation above the token admission budget. Which observation distinguishes the repair from a default-case-only fix?
5. Explain the contract in 03_private_checkpoints.py using one claim from its input cases.
6. Diagnose this broken behavior: Apply the requested thread-retention deletion. Which observation distinguishes the repair from a default-case-only fix?

<details>
<summary>Answers</summary>

1. Claim text and retrieved documents are untrusted data. A structured schema rejects extra authority fields and impossible amounts, while deterministic rules select routes. Neither a model's confidence nor a sentence saying 'approved' grants permission. Tool capabilities are independently restricted to the minimum required evidence reads.
2. Preserve validated amounts before applying deterministic routing. Compare the normal case with the boundary fixtures and identify the first differing update.
3. Admission checks reject a planned operation that exceeds the configured call or estimated-token budget. They supplement, rather than replace, runtime model/tool limits and recursion bounds. The API separately verifies role, current interrupt identity, and confirmed coverage before recording a payload-bound synthetic effect. Token estimates are conservative planning inputs, not a guaranteed hosted bill.
4. Reject an operation above the token admission budget. Compare the normal case with the boundary fixtures and identify the first differing update.
5. EncryptedSerializer encrypts serialized checkpoint payloads using an externally supplied key. The example creates an ephemeral key and never returns it. Minimize PII before storage; encryption does not hide every database field or replace access control, key rotation, and retention. A wrong key fails authentication, and deleting a thread is separate from deleting Store memories and backups.
6. Apply the requested thread-retention deletion. Compare the normal case with the boundary fixtures and identify the first differing update.

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

- [untrusted input official guide](https://docs.langchain.com/oss/python/langchain/guardrails)
- [approval and limits official guide](https://docs.langchain.com/oss/python/langgraph/interrupts)
- [private checkpoints official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)

## Next:

Continue to [module 22: Deployment](../../modules/22_deployment/README.md).
