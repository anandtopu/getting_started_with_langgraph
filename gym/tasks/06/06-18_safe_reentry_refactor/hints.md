# Hints

## Hint 1

A clerk rereads the form after approval; rereading must not send a second payment notice. Compare the first differing field with the task's required behavior.

## Hint 2

Separate checkpointed work still needs an idempotent effect contract. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: notifications.setdefault(key, "Synthetic approval notification"). Check every boundary input after the repair; a default-case pass alone is insufficient.
