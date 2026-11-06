"""A grounded tool-using policy agent with customer-scoped memory.

Run: uv run python capstones/02_policy_qa_with_memory/solution.py
Expected: home.md citation and remembered sms preference. LLM: local scripted fake.
"""

import re

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.runtime import Runtime
from langgraph.store.memory import InMemoryStore
from typing_extensions import TypedDict

from common.config import ROOT
from common.copilot.v06 import CustomerContext
from common.models import get_chat_model
from common.pretty import print_state


class QAState(TypedDict):
    question: str
    answer: str
    citations: list[str]
    preference: str


def retrieve(question: str) -> list[dict]:
    tokens = set(re.findall(r"[a-z]+", question.lower())) - {"the", "a", "is", "what", "my"}
    ranked = []
    for path in sorted((ROOT / "data/policies").glob("*.md")):
        content = path.read_text("utf-8")
        words = set(re.findall(r"[a-z]+", content.lower()))
        score = len(tokens & words) + (10 if path.stem in tokens else 0)
        if score:
            ranked.append((score, {"source": path.name, "text": content}))
    return [row for _, row in sorted(ranked, key=lambda item: -item[0])[:1]]


def build_graph(store=None, checkpointer=None):
    store = store if store is not None else InMemoryStore()

    def answer_question(state, runtime: Runtime[CustomerContext]):
        evidence = retrieve(state["question"])

        @tool
        def search_policies(question: str) -> list[dict]:
            """Return synthetic policy passages and their filenames; never authorize payouts."""
            return retrieve(question)

        text = evidence[0]["text"] if evidence else "No supporting policy passage; ask an adjuster."
        # The fake quotes retrieved evidence. A live model still needs citation verification.
        agent = create_agent(
            model=get_chat_model(
                responses=[
                    AIMessage(
                        content="",
                        tool_calls=[
                            {
                                "name": "search_policies",
                                "args": {"question": state["question"]},
                                "id": "retrieve-1",
                            }
                        ],
                    ),
                    AIMessage(content=text),
                ]
            ),
            tools=[search_policies],
            checkpointer=False,
        )
        result = agent.invoke(
            {"messages": [HumanMessage(content=state["question"])]},
            {"recursion_limit": 8},
            version="v2",
        )
        memory = store.get(("customers", runtime.context.customer_id), "contact")
        return {
            "answer": result.value["messages"][-1].content,
            "citations": [item["source"] for item in evidence],
            "preference": memory.value["preference"] if memory else "email",
        }

    graph = StateGraph(QAState, context_schema=CustomerContext)
    graph.add_node("retrieve_and_answer", answer_question)
    graph.add_edge(START, "retrieve_and_answer")
    graph.add_edge("retrieve_and_answer", END)
    return graph.compile(checkpointer=checkpointer or InMemorySaver(), store=store)


def run(case=None):
    case = {"question": "What is the home deductible?", "customer_id": "CUS-0001", **(case or {})}
    store = InMemoryStore()
    store.put(("customers", "CUS-0001"), "contact", {"preference": "sms"})
    graph = build_graph(store)
    config = {"configurable": {"thread_id": case["customer_id"] + ":qa"}}
    context = CustomerContext(case["customer_id"])
    graph.invoke({"question": case["question"]}, config, context=context, version="v2")
    result = graph.invoke(
        {"question": case["question"]}, config, context=context, version="v2"
    ).value
    return {key: result[key] for key in ("answer", "citations", "preference")}


def main():
    print_state(run())


if __name__ == "__main__":
    main()
