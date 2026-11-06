"""Shared ownership records, transactional effect keys, and cross-worker thread leases."""

import json
from contextlib import asynccontextmanager

from common.service import BusyThread, Principal


class PostgresLedger:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def record(self, key: str, payload: dict) -> bool:
        import psycopg

        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        with psycopg.connect(self.connection_string) as connection:
            inserted = connection.execute(
                "INSERT INTO larkspur_effects (effect_key, payload) VALUES (%s, %s) ON CONFLICT DO NOTHING RETURNING effect_key",
                (key, encoded),
            ).fetchone()
            row = connection.execute(
                "SELECT payload FROM larkspur_effects WHERE effect_key = %s", (key,)
            ).fetchone()
            if row[0] != encoded:
                raise ValueError("Idempotency key reused with a different payload")
            return inserted is not None


class PostgresRegistry:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.ledger = PostgresLedger(connection_string)

    async def connect(self):
        from psycopg import AsyncConnection

        return await AsyncConnection.connect(self.connection_string, autocommit=True)

    async def setup(self):
        async with await self.connect() as connection:
            await connection.execute(
                "CREATE TABLE IF NOT EXISTS larkspur_threads (thread_id TEXT PRIMARY KEY, customer_id TEXT NOT NULL, claim TEXT NOT NULL)"
            )
            await connection.execute(
                "CREATE TABLE IF NOT EXISTS larkspur_effects (effect_key TEXT PRIMARY KEY, payload TEXT NOT NULL)"
            )

    async def create(self, thread_id: str, principal: Principal, claim: dict):
        if claim["customer_id"] != principal.customer_id:
            raise PermissionError("Claim belongs to another customer")
        async with await self.connect() as connection:
            cursor = await connection.execute(
                "INSERT INTO larkspur_threads VALUES (%s, %s, %s) ON CONFLICT DO NOTHING RETURNING thread_id",
                (thread_id, principal.customer_id, json.dumps(claim)),
            )
            if await cursor.fetchone() is None:
                raise ValueError("Thread already exists")

    async def claim(self, thread_id: str, principal: Principal) -> dict:
        async with await self.connect() as connection:
            cursor = await connection.execute(
                "SELECT customer_id, claim FROM larkspur_threads WHERE thread_id = %s", (thread_id,)
            )
            row = await cursor.fetchone()
        if row is None or row[0] != principal.customer_id:
            raise PermissionError("Thread is unavailable")
        return json.loads(row[1])

    @asynccontextmanager
    async def guard(self, thread_id: str):
        async with await self.connect() as connection, connection.transaction():
            cursor = await connection.execute(
                "SELECT pg_try_advisory_xact_lock(hashtextextended(%s, 0))", (thread_id,)
            )
            if not (await cursor.fetchone())[0]:
                raise BusyThread("Another worker owns this thread")
            yield
