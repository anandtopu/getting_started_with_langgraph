# Hints

## Hint 1

Each customer has a separate waiting folder, and an inspection copy cannot alter the archived original. Compare the first differing field with the task's required behavior.

## Hint 2

Validate the resumed decision before updating approval state. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: type(resume) is not bool. Check every boundary input after the repair; a default-case pass alone is insufficient.
