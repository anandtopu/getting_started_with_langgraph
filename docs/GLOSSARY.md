# Glossary

**State.** Named data a graph carries between steps.

**Channel.** One state field together with the rule for accepting its updates.

**Node.** A unit of work that reads state and returns changes.

**Edge.** A connection that schedules later work.

**Conditional edge.** A connection whose destination depends on a routing function.

**Router.** A function that chooses the next node or completion.

**Partial update.** A dictionary containing only fields a node changes.

**Reducer.** A function that combines an old field value and a new update.

**Overwrite.** Replacing a field instead of accumulating its previous value.

**Associativity.** Combining updates in different groupings gives the same result.

**Commutativity.** Swapping update order leaves the result unchanged.

**Idempotence.** Repeating an operation has the same effect as doing it once.

**Superstep.** A batch of scheduled nodes that read the same previous state boundary.

**Barrier.** The point where sibling work finishes and its updates are merged.

**Fan-out.** Scheduling several independent branches.

**Fan-in.** Combining or continuing after parallel branches.

**Map-reduce.** Apply work to many items, then combine their results.

**Send.** An instruction that schedules a node with a particular input.

**Command.** An object carrying control-flow changes, state updates, or resume values.

**START.** The graph's entry connection.

**END.** The graph's completion destination.

**Compile.** Turn a graph definition into an executable graph.

**Invoke.** Run a graph until it completes or pauses.

**GraphOutput.** The v2 invocation wrapper containing values and interrupts.

**Stream.** A sequence of observations emitted while work executes.

**Stream namespace.** The location of an event within nested graph execution.

**Checkpoint.** A saved execution boundary used for inspection and recovery.

**Checkpointer.** The component that stores and retrieves checkpoints.

**Thread.** The persistent history associated with one configured thread ID.

**Snapshot.** An inspectable view of state and pending work at a saved boundary.

**Pending write.** A recorded task result that can survive another task's failure.

**Interrupt.** A durable request to stop and wait for an external answer.

**Resume.** Continue a saved execution with the requested answer.

**Replay.** Execute from a saved boundary; later work may run again.

**Fork.** Continue an alternative history from an earlier checkpoint.

**Durability.** How reliably committed execution progress survives process failure.

**Subgraph.** A graph used as a component inside another graph.

**Adapter.** Code that translates one component's input and output into another's schema.

**Private state.** Internal fields intentionally excluded from a public component boundary.

**Context.** Trusted invocation data such as identity or dependencies, separate from mutable state.

**Runtime.** The node's access to invocation context, Store, and execution facilities.

**Store.** A namespaced place for memory shared across threads.

**Namespace.** A tuple or path that groups records, often by customer and memory type.

**Short-term memory.** Conversation state retained within one thread.

**Long-term memory.** Information retained across conversations or threads.

**Semantic memory.** Stored facts or preferences, rather than an event transcript.

**Episodic memory.** Stored descriptions of earlier events or experiences.

**Embedding.** A numeric vector representing content for similarity comparisons.

**Vector search.** Retrieval using similarity between numeric representations.

**RAG.** Retrieval-augmented generation: supply retrieved evidence when producing an answer.

**Citation.** A reference to the evidence supporting a statement.

**LLM.** A model that predicts and generates language-like sequences.

**Token.** A unit of model input or output, often part of a word.

**Context window.** The maximum input and output context a model can handle together.

**Temperature.** A generation setting affecting sampling; zero still does not guarantee a provider's reproducibility.

**Prompt.** Instructions and content supplied to a model.

**System message.** Instructions describing the model's role or behavior.

**Human message.** A message representing user input.

**AI message.** A model response, possibly containing tool calls.

**Tool message.** The result associated with a particular tool-call ID.

**Tool.** A callable capability with a declared input schema and description.

**Tool call.** A model's structured request to invoke a named capability.

**Structured output.** A response validated against an explicit schema.

**Agent.** A system that can choose actions dynamically within given capabilities and limits.

**Workflow.** A process whose control-flow structure is chosen by its author.

**ReAct loop.** An agent cycle of model decisions, tool execution, and model continuation.

**Middleware.** Hooks around agent execution for state changes, policies, or interception.

**Supervisor.** A coordinator that chooses which scoped specialist to consult.

**Handoff.** A transfer of control and selected context to another agent or graph.

**Functional API.** Durable orchestration expressed with entrypoint and task functions.

**Future.** A handle for a result that may still be computing.

**Retry.** A bounded repeat after a selected transient failure.

**Timeout.** A limit on how long an operation may run.

**Cancellation.** A request to stop work, requiring cleanup of resources.

**Backoff.** Increasing delays between retries to avoid overwhelming a failing dependency.

**Idempotency key.** A stable operation identifier used to reject duplicate or conflicting effects.

**Lease.** Temporary exclusive ownership of work, such as one running thread.

**MCP.** Model Context Protocol, a standard way to expose tools and resources to clients.

**stdio transport.** A local process protocol carried over standard input and output.

**SSE.** Server-sent events: a one-way HTTP stream from server to client.

**Evaluation.** Measuring behavior against explicit expected outcomes or criteria.

**Trajectory.** The ordered messages and tool actions taken during an agent run.

**Trace.** A diagnostic record of nested operations, inputs, outputs, and timing.

**Prompt injection.** Untrusted text attempting to redirect the system's instructions or authority.

**Authorization.** The server's decision about which authenticated actor may perform an action.

**Schema validation.** Checking that a value has the required fields, types, and constraints.

**Delta channel.** A Beta channel that retains incremental writes and reconstructs accumulated state.

**Beta.** An explicitly experimental API whose contract may change before stabilization.
