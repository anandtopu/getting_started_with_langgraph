# Hints

## Hint 1

The main case and specialist folders have separate progress feeds, even when one screen presents them together. Compare the first differing field with the task's required behavior.

## Hint 2

Read the final model message from the completed output projection. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: output["messages"][-1].text. Check every boundary input after the repair; a default-case pass alone is insufficient.
