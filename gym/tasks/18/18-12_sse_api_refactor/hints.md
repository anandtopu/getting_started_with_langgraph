# Hints

## Hint 1

A numbered progress bulletin is useful only when it goes to the right customer and references the current approval form. Compare the first differing field with the task's required behavior.

## Hint 2

Compare the payload field after decoding, not its event category. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: decoded[0]["data"]["node"] == case["note"]. Check every boundary input after the repair; a default-case pass alone is insufficient.
