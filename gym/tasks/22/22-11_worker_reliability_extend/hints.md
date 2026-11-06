# Hints

## Hint 1

Any adjuster may pick up the durable folder, but only one holds its checkout card at a time. Compare the first differing field with the task's required behavior.

## Hint 2

Exercise and reject idempotency-key reuse with a changed payload. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: + int(case["changed_payload"]). Check every boundary input after the repair; a default-case pass alone is insufficient.
