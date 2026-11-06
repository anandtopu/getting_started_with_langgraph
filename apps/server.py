"""Build the configured local or Postgres app: uvicorn apps.server:build_app --factory."""

import os
from contextlib import asynccontextmanager
from pathlib import Path

from apps.api import create_app
from common.copilot.v11 import build_graph
from common.service import Principal, ThreadRegistry


def build_app():
    customer_token = os.environ.get("LARKSPUR_CUSTOMER_TOKEN", "")
    adjuster_token = os.environ.get("LARKSPUR_ADJUSTER_TOKEN", "")
    if not customer_token or not adjuster_token or customer_token == adjuster_token:
        raise ValueError("Set distinct customer and adjuster tokens; see .env.example")
    customer_id = os.environ.get("LARKSPUR_CUSTOMER_ID", "CUS-0001")
    tokens = {
        customer_token: Principal("demo-customer", customer_id, "customer"),
        adjuster_token: Principal("demo-adjuster", customer_id, "adjuster"),
    }

    @asynccontextmanager
    async def resources():
        connection_string = os.environ.get("DATABASE_URL")
        if connection_string:
            from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
            from langgraph.store.postgres.aio import AsyncPostgresStore

            from common.postgres_service import PostgresRegistry

            registry = PostgresRegistry(connection_string)
            await registry.setup()
            async with (
                AsyncPostgresSaver.from_conn_string(connection_string) as saver,
                AsyncPostgresStore.from_conn_string(connection_string) as store,
            ):
                await saver.setup()
                await store.setup()
                yield build_graph(saver, store), registry
        else:
            from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

            directory = Path(os.environ.get("LARKSPUR_STATE_DIR", "workspace/server"))
            directory.mkdir(parents=True, exist_ok=True)
            registry = ThreadRegistry(directory / "ownership.db")
            async with AsyncSqliteSaver.from_conn_string(
                str(directory / "checkpoints.db")
            ) as saver:
                yield build_graph(saver), registry

    return create_app(tokens=tokens, resource_factory=resources)
