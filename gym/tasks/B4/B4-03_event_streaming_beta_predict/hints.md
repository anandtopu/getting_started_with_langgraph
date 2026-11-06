# Hints

## Hint 1

The main case and specialist folders have separate progress feeds, even when one screen presents them together. Compare the first differing field with the task's required behavior.

## Hint 2

Read child model messages through their subgraph projection. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: for child in stream.subgraphs for message in child.messages. Check every boundary input after the repair; a default-case pass alone is insufficient.
