# Quiz

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
