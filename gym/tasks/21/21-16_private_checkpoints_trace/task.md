# 21-16 — Diagnose private checkpoints from execution evidence

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

EncryptedSerializer encrypts serialized checkpoint payloads using an externally supplied key. The example creates an ephemeral key and never returns it. Minimize PII before storage; encryption does not hide every database field or replace access control, key rotation, and retention. A wrong key fails authentication, and deleting a thread is separate from deleting Store memories and backups.

## Your task

Diagnose private checkpoints from execution evidence Inspect trace.json before reading trace.py. The node updates are captured locally from execution, with superstep labels where available; siblings can finish in either order. Use the observed result for plain-Python or child-process examples. Explain the first incorrect transition, not just the final symptom.

## Inputs and acceptance

```json
[
  {
    "note": "Synthetic customer phone 555-0100",
    "delete": true,
    "wrong_key": false
  },
  {
    "note": "Synthetic customer phone 555-0100",
    "delete": false,
    "wrong_key": false
  }
]
```

Choose the cause supported by the trace. Set `cause` to exactly one of these descriptions, and preserve the listed observation order:

- "Install encryption on the actual checkpointer, not just a standalone serialization demo."
- "Apply the requested thread-retention deletion."
- "Verify that a wrong encryption key cannot restore the payload."
- "Check exact restoration after successful authenticated decryption."

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 21-16
uv run gym check 21-16
uv run gym hint 21-16
```

## Reading

[Module lesson](../../../../modules/21_security_and_guardrails/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
