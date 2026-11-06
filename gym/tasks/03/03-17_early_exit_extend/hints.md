# Hints

## Hint 1

A rejected form still receives a reason stamp before leaving the queue. Compare the first differing field with the task's required behavior.

## Hint 2

Duplicate submissions need an explicit terminal reason. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: "duplicate"
        if state["duplicate_of"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
