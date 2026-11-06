# Hints

## Hint 1

Verify the measurements before asking the writer to prepare a settlement letter. Compare the first differing field with the task's required behavior.

## Hint 2

Stop the chain when the fact gate fails. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "draft" if state["accepted"] else END. Check every boundary input after the repair; a default-case pass alone is insufficient.
