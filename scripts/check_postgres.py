"""Check real Postgres ownership, cross-worker exclusion, memory, and effect keys."""

import asyncio
import os
import uuid

from langgraph.store.postgres.aio import AsyncPostgresStore

from common.data import load_submission
from common.postgres_service import PostgresRegistry
from common.service import BusyThread, Principal


async def main():
    connection = os.environ["DATABASE_URL"]
    first, second = PostgresRegistry(connection), PostgresRegistry(connection)
    await first.setup()
    thread = "probe-" + uuid.uuid4().hex
    owner = Principal("probe", "CUS-0001", "adjuster")
    await first.create(thread, owner, load_submission(1))
    assert (await second.claim(thread, owner))["claim_id"] == "CLM-0001"
    async with first.guard(thread):
        try:
            async with second.guard(thread):
                raise AssertionError("Two workers acquired one thread")
        except BusyThread:
            pass
    async with second.guard(thread):
        assert first.ledger.record(thread, {"amount_cents": 1})
        assert not second.ledger.record(thread, {"amount_cents": 1})
        try:
            second.ledger.record(thread, {"amount_cents": 2})
            raise AssertionError("A conflicting payload reused an effect key")
        except ValueError:
            pass
    async with AsyncPostgresStore.from_conn_string(connection) as store:
        await store.setup()
        await store.aput(("probe", thread), "preference", {"contact": "sms"})
    async with AsyncPostgresStore.from_conn_string(connection) as store:
        assert (await store.aget(("probe", thread), "preference")).value == {"contact": "sms"}
        await store.adelete(("probe", thread), "preference")
    async with await first.connect() as database:
        row = await (
            await database.execute(
                "SELECT COUNT(*) FROM larkspur_effects WHERE effect_key LIKE 'payment:%'"
            )
        ).fetchone()
        assert row[0] == 1, row
        await database.execute("DELETE FROM larkspur_threads WHERE thread_id = %s", (thread,))
        await database.execute("DELETE FROM larkspur_effects WHERE effect_key = %s", (thread,))
    print("PASS Postgres ownership, leases, payload binding, durable Store, and one payment effect")


if __name__ == "__main__":
    asyncio.run(main())
