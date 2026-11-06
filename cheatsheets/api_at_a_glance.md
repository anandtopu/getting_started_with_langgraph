# LangGraph | API at a glance

## StateGraph(State)

Define named state channels and optional input/output/context schemas.

## add_node / add_edge

Register work and fixed connections. START enters; END completes.

## add_conditional_edges

Map a router's result to the next destination; cover every possible result.

## Command / Send

Update and route, resume an interrupt, or schedule parameterized parallel work.

## compile(checkpointer=...)

Create a runnable with an explicit persistence lifecycle.

## invoke / ainvoke

Pass version='v2'; inspect result.value and result.interrupts.

## stream / astream

Pass version='v2'; handle each part's type, ns, and data.

## interrupt / Command(resume=...)

Save a request, then continue the same thread with validated answers.

## get_state / get_state_history

Inspect current and earlier snapshots, including next scheduled work.

## update_state

Create a state update at a selected boundary; use checkpoint configuration deliberately.

## Runtime / Store

Read trusted context and scoped cross-thread memory inside a node.

## entrypoint / task

Use ordinary Python orchestration with durable task results.

## create_agent

Build a bounded model/tool loop from langchain.agents and the shared model factory.

## Beta: stream_events / DeltaChannel

Optional B4 only; v3 events use method/params, unlike core v2 parts.

Verified course API family: 2026-11-06. See docs/VERIFICATION_NOTES.md and the lockfiles.
