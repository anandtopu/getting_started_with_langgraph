# Hints

## Hint 1

Keep the receipt log, the current folder, and the clerk's progress announcement in separate columns. Compare the first differing field with the task's required behavior.

## Hint 2

The state payload is inside data, not at the envelope root. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: part["data"].get("status", "input"). Check every boundary input after the repair; a default-case pass alone is insufficient.
