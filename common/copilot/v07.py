"""Version 07: reusable fraud inspection and private specialist agents."""

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.store.memory import InMemoryStore
from langgraph.types import Command

from common.copilot import v06
from common.data import load_submission
from common.models import get_chat_model


class TeamState(v06.MemoryClaimState):
    risk_flags: list[str]
    specialist_reports: list[dict]


def build_fraud_graph():
    def inspect(state: TeamState) -> dict:
        claim = state["claim"]
        flags = list(claim.get("fraud_indicators", []))
        if not claim.get("documents"):
            flags.append("missing_evidence")
        if claim["amount_cents"] > 500000:
            flags.append("high_value")
        return {"risk_flags": sorted(set(flags))}

    graph = StateGraph(TeamState)
    graph.add_node("inspect_evidence", inspect)
    graph.add_edge(START, "inspect_evidence")
    graph.add_edge("inspect_evidence", END)
    return graph.compile()


def consult_specialists(state: TeamState) -> dict:
    @tool
    def fraud_analyst() -> str:
        """Review rule flags without access to customer contact details."""
        agent = create_agent(
            model=get_chat_model(
                responses=[
                    AIMessage(
                        content="Rule flags require evidence review; they are not proof of fraud."
                    )
                ]
            ),
            tools=[],
            checkpointer=False,
        )
        return (
            agent.invoke(
                {"messages": [HumanMessage(content=str(state["risk_flags"]))]}, version="v2"
            )
            .value["messages"][-1]
            .content
        )

    @tool
    def communication_specialist() -> str:
        """Review the customer letter's tone without access to the claim database."""
        agent = create_agent(
            model=get_chat_model(
                responses=[
                    AIMessage(content="The letter is respectful and makes no payment promise.")
                ]
            ),
            tools=[],
            checkpointer=False,
        )
        return (
            agent.invoke({"messages": [HumanMessage(content=state["letter"])]}, version="v2")
            .value["messages"][-1]
            .content
        )

    tools = [fraud_analyst, communication_specialist]
    supervisor = create_agent(
        model=get_chat_model(
            responses=[
                AIMessage(
                    content="",
                    tool_calls=[
                        {"name": item.name, "args": {}, "id": "team-" + str(index)}
                        for index, item in enumerate(tools)
                    ],
                ),
                AIMessage(
                    content="Specialist review complete; existing authorization remains unchanged."
                ),
            ]
        ),
        tools=tools,
        checkpointer=False,
    )
    value = supervisor.invoke(
        {"messages": [HumanMessage(content="Review the scoped claim evidence and letter.")]},
        {"recursion_limit": 12},
        version="v2",
    ).value
    return {
        "specialist_reports": [
            {"specialist": item.name, "report": item.content}
            for item in value["messages"]
            if item.type == "tool"
        ],
        "audit": ["specialists_consulted"],
    }


def build_graph(checkpointer=None, store=None):
    graph = StateGraph(TeamState, context_schema=v06.CustomerContext)
    graph.add_node("intake_policy_memory", v06.build_graph(checkpointer=True, store=store))
    graph.add_node("fraud_review", build_fraud_graph())
    graph.add_node("consult_specialists", consult_specialists)
    graph.add_edge(START, "intake_policy_memory")
    graph.add_edge("intake_policy_memory", "fraud_review")
    graph.add_edge("fraud_review", "consult_specialists")
    graph.add_edge("consult_specialists", END)
    return graph.compile(
        checkpointer=checkpointer if checkpointer is not None else InMemorySaver(),
        store=store if store is not None else InMemoryStore(),
    )


def run(claim=None, *, approved=True):
    claim = load_submission(1) if claim is None else claim
    graph = build_graph()
    config = {"configurable": {"thread_id": claim["claim_id"]}}
    context = v06.CustomerContext(claim["customer_id"])
    result = graph.invoke(
        {"claim": claim, "audit": [], "findings": []}, config, context=context, version="v2"
    )
    if result.interrupts:
        result = graph.invoke(
            Command(resume={"approved": approved}), config, context=context, version="v2"
        )
    return result.value
