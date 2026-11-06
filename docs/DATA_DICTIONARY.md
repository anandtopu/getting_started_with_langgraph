# Synthetic data dictionary

All identifiers and events are fictional. Monetary values are nonnegative integer cents. The five policy Markdown files are the educational source of coverage rules; a category match alone is not coverage approval.

| Table | Key | Meaning |
| --- | --- | --- |
| customers | customer_id | Fictional display name, reserved example-domain email, contact preference |
| policies | policy_id | Customer ownership, product code, payout limit, deductible, effective date |
| claims | claim_id | Customer/policy links, type, text, amount, loss date, route, duplicate link, review indicators |
| claim_documents | document_id | Claim ownership and paths to paired text/PDF artifacts |
| payments | payment_id | Proposed synthetic amount, unique idempotency key, optional adjuster reference |
| adjusters | adjuster_id | Fictional name and review specialty |

There are 500 claims, 100 customers, 100 policies, five adjusters, 30 document records, and ten proposed ledger entries. The 60 incoming submissions include explicit missing fields, duplicates, and review indicators. Null or empty values are intentional. A fraud indicator means review is needed, not that wrongdoing is proven.

The first 30 claims have corresponding document fixtures; later submissions may await documents. Duplicate submissions can reference the original claim's documents. The database and a submission represent related snapshots; absence of an attachment in a submission does not erase a document already held by the claims system.

The generator uses seed 41723 and a fixed date anchor. All email addresses use the reserved .example domain. PDF dates and identifiers are fixed. The manifest hashes committed files. SQLite header bytes may differ across writer versions; cross-platform regeneration tests compare its logical rows.

Golden routing/state rows are generated from the deterministic reference rules. Independent boundary tests cover those rules so a defect cannot validate itself only through generated expected output. Payout golden cases are explicit hand-checkable examples. Security cases require zero payment writes without trusted approval.

Use common.data to read fixtures. It opens SQLite read-only and rejects dataset path traversal. Copy data into an ignored workspace or temporary directory for mutation exercises.
