"""A small teaching runner: barriers, channels, reducers, checkpoints, and single-node pauses.

This is deliberately not a production engine. It has no async work, distributed leases,
pending-write crash recovery, streaming protocol, serialization, or parallel interrupts.
"""

from collections.abc import Callable
from copy import deepcopy
from dataclasses import dataclass
from typing import Any


class WriteConflict(ValueError):
    """Several parallel nodes wrote an overwrite channel."""


class Pause(Exception):
    def __init__(self, request):
        self.request = request
        super().__init__("The teaching runner is waiting for input")


@dataclass
class Snapshot:
    values: dict
    pending: list[str]
    step: int
    request: Any = None


class MiniGraph:
    def __init__(
        self,
        nodes: dict[str, Callable],
        edges: dict[str, list[str]],
        start: list[str],
        reducers: dict[str, Callable] | None = None,
    ):
        self.nodes = nodes
        self.edges = edges
        self.start = start
        self.reducers = reducers or {}
        self.checkpoints: dict[str, list[Snapshot]] = {}

    def latest(self, thread_id: str) -> Snapshot:
        if thread_id not in self.checkpoints:
            raise ValueError("Unknown teaching thread")
        return deepcopy(self.checkpoints[thread_id][-1])

    def save(self, thread_id: str, snapshot: Snapshot):
        self.checkpoints.setdefault(thread_id, []).append(deepcopy(snapshot))

    def run(self, values: dict | None, *, thread_id="claim", resume=None, limit=20) -> Snapshot:
        if type(limit) is not int or limit < 1:
            raise ValueError("The superstep limit must be a positive integer")
        if values is None:
            current = self.latest(thread_id)
        else:
            current = Snapshot(deepcopy(values), list(self.start), 0)
            self.save(thread_id, current)
        for _ in range(limit):
            if not current.pending:
                return deepcopy(current)
            before = deepcopy(current.values)
            writes: dict[str, list] = {}
            following = []
            for name in sorted(current.pending):
                try:
                    # KEY IDEA: every sibling reads the same previous-boundary snapshot.
                    update = self.nodes[name](deepcopy(before), resume)
                except Pause as pause:
                    if len(current.pending) != 1:
                        raise ValueError(
                            "This mini runner only pauses a single-node step"
                        ) from pause
                    current.request = pause.request
                    self.save(thread_id, current)
                    return deepcopy(current)
                if not isinstance(update, dict):
                    raise TypeError("Nodes return partial dictionaries")
                for key, value in update.items():
                    writes.setdefault(key, []).append(value)
                following.extend(self.edges.get(name, []))
            after = deepcopy(before)
            for key, updates in writes.items():
                if key not in self.reducers and len(updates) > 1:
                    raise WriteConflict("Parallel writes require a reducer: " + key)
                if key in self.reducers:
                    value = after.get(key)
                    for update in updates:
                        value = self.reducers[key](value, update)
                    after[key] = value
                else:
                    after[key] = updates[0]
            current = Snapshot(after, sorted(set(following)), current.step + 1)
            self.save(thread_id, current)
            resume = None
        if not current.pending:
            return deepcopy(current)
        raise RuntimeError("Teaching superstep budget exhausted")
