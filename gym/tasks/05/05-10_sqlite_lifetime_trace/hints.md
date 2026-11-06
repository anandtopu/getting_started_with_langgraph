# Hints

## Hint 1

A desk notebook disappears with the desk; a closed archive file can be reopened by the next shift. Compare the first differing field with the task's required behavior.

## Hint 2

A compiled graph cannot use a saver whose connection has closed. Inspect the operation that owns this update or routing choice.

## Hint 3

The reference contract uses this operation: with SqliteSaver.from_conn_string(database) as saver:
        result = build_graph(saver).invoke(payload, config, version="v2").value. Check every boundary input after the repair; a default-case pass alone is insufficient.
