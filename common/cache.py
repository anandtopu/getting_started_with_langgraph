"""An educational in-process cache with an injected clock for deterministic TTL tests."""

from collections.abc import Callable, Mapping, Sequence
from copy import deepcopy
from threading import RLock
from typing import Any

from langgraph.cache.base import BaseCache, FullKey, Namespace


class ClockCache(BaseCache):
    def __init__(self, clock: Callable[[], float]):
        super().__init__()
        self.clock = clock
        self.entries: dict[FullKey, tuple[Any, float | None]] = {}
        self.lock = RLock()

    def get(self, keys: Sequence[FullKey]) -> dict[FullKey, Any]:
        found = {}
        with self.lock:
            for key in keys:
                if key in self.entries:
                    value, expiry = self.entries[key]
                    if expiry is None or self.clock() < expiry:
                        found[key] = deepcopy(value)
                    else:
                        del self.entries[key]
        return found

    def set(self, keys: Mapping[FullKey, tuple[Any, int | None]]) -> None:
        with self.lock:
            for key, (value, ttl) in keys.items():
                self.entries[key] = (deepcopy(value), None if ttl is None else self.clock() + ttl)

    def clear(self, namespaces: Sequence[Namespace] | None = None) -> None:
        with self.lock:
            if namespaces is None:
                self.entries.clear()
            else:
                self.entries = {
                    key: value for key, value in self.entries.items() if key[0] not in namespaces
                }

    async def aget(self, keys: Sequence[FullKey]) -> dict[FullKey, Any]:
        return self.get(keys)

    async def aset(self, keys: Mapping[FullKey, tuple[Any, int | None]]) -> None:
        self.set(keys)

    async def aclear(self, namespaces: Sequence[Namespace] | None = None) -> None:
        self.clear(namespaces)
