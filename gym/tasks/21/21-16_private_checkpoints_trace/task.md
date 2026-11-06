# 21-16 — Trace private checkpoints: Apply the requested thread-retention deletion.

Type: trace. Difficulty: medium. No live model, key, or network is required.

## The claim scenario

EncryptedSerializer encrypts serialized checkpoint payloads using an externally supplied key. The example creates an ephemeral key and never returns it. Minimize PII before storage; encryption does not hide every database field or replace access control, key rotation, and retention. A wrong key fails authentication, and deleting a thread is separate from deleting Store memories and backups.

## Your task

Apply the requested thread-retention deletion. Read trace.py before completing the answer JSON. Explain the first incorrect transition, not just the final symptom.

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

The suite checks more than the default claim. Keep identities, boundary behavior, and isolation intact. A Design pass includes a separate self-review and is not an automatic architecture-quality judgment.

## Commands

```text
uv run gym start 21-16
uv run gym check 21-16
uv run gym hint 21-16
```

## Reading

[Module lesson](../../../../modules/21_security_and_guardrails/README.md) · [Official guide](https://docs.langchain.com/oss/python/langgraph/checkpointers)
