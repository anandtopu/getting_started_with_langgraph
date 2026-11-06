"""Fake-model contracts are exercised through real LangChain and LangGraph calls."""

import pytest
from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.graph import END, START, MessagesState, StateGraph
from pydantic import ValidationError

from common.fakes import ScriptExhaustedError
from common.models import get_chat_model
from common.schemas import ClaimExtraction


def test_fake_exhaustion_and_reset():
    model = get_chat_model()
    assert model.invoke("claim").content == "Larkspur received your synthetic claim."
    with pytest.raises(ScriptExhaustedError):
        model.invoke("unexpected second call")
    model.reset()
    assert model.invoke("claim").id == "ack-1"
    assert model.calls == 1


def test_fake_does_not_mutate_input_or_share_responses():
    message = HumanMessage(content="claim")
    response = AIMessage(content="accepted")
    one = get_chat_model(responses=[response])
    two = get_chat_model(responses=[response])
    received = one.invoke([message])
    received.content = "changed"
    assert response.content == "accepted"
    assert two.invoke([message]).content == "accepted"
    assert one.history[0][0].content == "claim"


def test_structured_output_validates_and_can_return_raw_error():
    parsed = (
        get_chat_model(scenario="extract").with_structured_output(ClaimExtraction).invoke("extract")
    )
    assert parsed.amount_cents == 125_000
    broken = get_chat_model(responses=[AIMessage(content='{"amount_cents": -1}')])
    result = broken.with_structured_output(ClaimExtraction, include_raw=True).invoke("extract")
    assert result["parsed"] is None
    assert isinstance(result["parsing_error"], ValidationError)
    with pytest.raises(ValidationError):
        get_chat_model(responses=[AIMessage(content="{}")]).with_structured_output(
            ClaimExtraction
        ).invoke("extract")


def test_streamed_text_and_tool_arguments_reassemble():
    expected = get_chat_model().invoke("claim")
    chunks = list(get_chat_model().stream("claim"))
    aggregate = chunks[0]
    for chunk in chunks[1:]:
        aggregate += chunk
    assert aggregate.content == expected.content

    model = get_chat_model(scenario="policy_lookup")
    chunks = list(model.stream("look up policy"))
    aggregate = chunks[0]
    for chunk in chunks[1:]:
        aggregate += chunk
    assert aggregate.tool_calls == [
        {
            "name": "lookup_policy",
            "args": {"policy_id": "POL-0001"},
            "id": "call-policy-1",
            "type": "tool_call",
        }
    ]


async def test_async_invoke_and_stream_are_offline():
    result = await get_chat_model().ainvoke("claim")
    pieces = [chunk.content async for chunk in get_chat_model().astream("claim")]
    assert "".join(pieces) == result.content


def test_real_create_agent_with_bound_fake_tools():
    calls = []

    @tool
    def lookup_policy(policy_id: str) -> str:
        """Look up a synthetic policy by its identifier."""
        calls.append(policy_id)
        return "Home policy: deductible 100000 cents."

    model = get_chat_model(scenario="policy_lookup")
    agent = create_agent(model=model, tools=[lookup_policy])
    output = agent.invoke({"messages": [HumanMessage(content="Check my policy.")]}, version="v2")
    assert calls == ["POL-0001"]
    assert len(output.value["messages"]) == 4
    assert output.value["messages"][-1].content.endswith("$1,000 deductible.")
    assert model.calls == 2


def test_unknown_scripted_tool_is_rejected():
    model = get_chat_model(scenario="policy_lookup").bind_tools([])
    with pytest.raises(ValueError, match="not bound"):
        model.invoke("claim")


def test_graph_emits_v2_message_parts_with_fake_tokens():
    model = get_chat_model()

    def acknowledge(state):
        return {"messages": [model.invoke(state["messages"])]}

    builder = StateGraph(MessagesState)
    builder.add_node("acknowledge", acknowledge)
    builder.add_edge(START, "acknowledge")
    builder.add_edge("acknowledge", END)
    graph = builder.compile()
    parts = list(
        graph.stream(
            {"messages": [HumanMessage(content="claim")]}, stream_mode="messages", version="v2"
        )
    )
    assert parts and all(part["type"] == "messages" for part in parts)
    assert all("ns" in part and "data" in part for part in parts)
    text = "".join(str(part["data"][0].content) for part in parts)
    assert text == "Larkspur received your synthetic claim."
