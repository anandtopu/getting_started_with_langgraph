"""Thread ownership and local concurrency policy, independent of model output."""

import asyncio
import json
import sqlite3
from contextlib import asynccontextmanager
from dataclasses import dataclass
from pathlib import Path

from common.effects import EffectLedger


@dataclass(frozen=True)
class Principal:
    principal_id: str
    customer_id: str
    role: str


class BusyThread(Exception):
    """Another run already owns this thread's execution lease."""


class ThreadRegistry:
    """Single-process SQLite development backend; Postgres supplies cross-worker locks."""

    def __init__(self, path: Path):
        self.path = path
        self.locks: dict[str, asyncio.Lock] = {}
        self.ledger = EffectLedger(path)
        connection = sqlite3.connect(path)
        try:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS threads (thread_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL, claim TEXT NOT NULL)"
            )
            connection.commit()
        finally:
            connection.close()

    async def create(self, thread_id: str, principal: Principal, claim: dict) -> None:
        if claim["customer_id"] != principal.customer_id:
            raise PermissionError("Claim belongs to another customer")
        connection = sqlite3.connect(self.path)
        try:
            connection.execute(
                "INSERT INTO threads VALUES (?, ?, ?)",
                (thread_id, principal.customer_id, json.dumps(claim)),
            )
            connection.commit()
        except sqlite3.IntegrityError:
            raise ValueError("Thread already exists") from None
        finally:
            connection.close()

    async def claim(self, thread_id: str, principal: Principal) -> dict:
        connection = sqlite3.connect(self.path)
        try:
            row = connection.execute(
                "SELECT customer_id, claim FROM threads WHERE thread_id = ?", (thread_id,)
            ).fetchone()
        finally:
            connection.close()
        if row is None or row[0] != principal.customer_id:
            raise PermissionError("Thread is not available to this customer")
        return json.loads(row[1])

    @asynccontextmanager
    async def guard(self, thread_id: str):
        lock = self.locks.setdefault(thread_id, asyncio.Lock())
        if lock.locked():
            raise BusyThread("A run is already active")
        await lock.acquire()
        try:
            yield
        finally:
            lock.release()
