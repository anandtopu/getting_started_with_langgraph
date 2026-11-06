# 21-04 — Diagnose untrusted input from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

Claim text and retrieved documents are untrusted data. A structured schema rejects extra authority fields and impossible amounts, while deterministic rules select routes. Neither a model's confidence nor a sentence saying 'approved' grants permission. Tool capabilities are independently restricted to the minimum required evidence reads.

## Your task

Diagnose untrusted input from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Approval pauses are labeled separately from failures. If no node update was observed, use the recorded result and program to locate a pre-execution rejection or a plain-Python/child-process fault. Explain the first broken contract and how it causes the observed result.

## Inputs and acceptance

```json
[
  {
    "extra_authority": false,
    "amount_cents": 600000
  },
  {
    "extra_authority": true,
    "amount_cents": 600000
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Do not let extracted text authorize a payment."
- "Preserve validated amounts before applying deterministic routing."
- "Expose and reject an unexpected authority field instead of silently hiding it from validation."
- "Keep model-visible tool capabilities read-only."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 21-04
uv run gym check 21-04
uv run gym hint 21-04
```

## Reading

[Module lesson](../../../../modules/21_security_and_guardrails/README.md) · [Official guide](https://docs.langchain.com/oss/python/langchain/guardrails)
