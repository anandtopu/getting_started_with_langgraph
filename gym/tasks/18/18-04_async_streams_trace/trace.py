"""Diagnose async streams from execution evidence. Run this file with Python. No live model or network."""

import asyncio

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.config import get_stream_writer
from langgraph.graph import END, START, MessagesState, StateGraph

from common.models import get_chat_model
from common.pretty import print_state

DEFAULT_CASE = {"text": "Your estimate is ready.", "cancel": True}
MODES = ["values", "updates", "messages", "custom", "checkpoints", "tasks", "debug"]


def build_graph(text="Your estimate is ready."):
    model = get_chat_model(responses=[AIMessage(content=text, id="notice")])

    async def notify(state: MessagesState, config: RunnableConfig):
        get_stream_writer()({"stage": "drafting"})
        return {"messages": [await model.ainvoke(state["messages"], config)]}

    graph = StateGraph(MessagesState)
    graph.add_node("notify", notify)
    graph.add_edge(START, "notify")
    graph.add_edge("notify", END)
    return graph.compile(checkpointer=InMemorySaver())


async def arun(case):
    kinds, text = set(), ""
    config = {"configurable": {"thread_id": "stream-demo"}}
    async for part in build_graph(case["text"]).astream(
        {"messages": [HumanMessage(content="Update me.")]},
        config,
        stream_mode=["updates"],
        version="v2",
    ):
        kinds.add(part["type"])
        if part["type"] == "messages":
            text += part["data"][0].content
    invoked = await build_graph(case["text"]).ainvoke(
        {"messages": [HumanMessage(content="Update me.")]}, config, version="v2"
    )
    cleaned, started = [], asyncio.Event()

    async def waiting_node(state: MessagesState):
        try:
            started.set()
            await asyncio.Event().wait()
        finally:
            cleaned.append("closed")

    if case["cancel"]:
        graph = (
            StateGraph(MessagesState)
            .add_node("wait", waiting_node)
            .add_edge(START, "wait")
            .add_edge("wait", END)
            .compile()
        )
        pending = asyncio.create_task(graph.ainvoke({"messages": []}, version="v2"))
        await started.wait()
        pending.cancel()
        try:
            await pending
        except asyncio.CancelledError:
            pass
    return {
        "kinds": sorted(kinds),
        "text": text,
        "matches_invoke": text == invoked.value["messages"][-1].content,
        "cancelled_cleanly": bool(cleaned),
    }


def run(case: dict | None = None) -> dict:
    return asyncio.run(arun(dict(DEFAULT_CASE if case is None else case)))


def main() -> None:
    try:
        print_state(run())
    except Exception as error:
        print_state({"observed_error": type(error).__name__})


if __name__ == "__main__":
    main()
