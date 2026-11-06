# Hints

## Hint 1

Each desk adds a note to the same claim folder rather than throwing the folder away. Compare the first differing field with the task's required behavior.

## Hint 2

Refactor mutation into a pure partial update. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: return {"description": state["description"].strip()}. Check every boundary input after the repair; a default-case pass alone is insufficient.
