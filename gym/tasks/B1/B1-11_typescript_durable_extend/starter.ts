// YOUR CODE HERE: repair the task contract.
/** Send, SQLite checkpoints, interrupts, and JavaScript streams. No LLM.
 * Run: node modules/bonus/B1_langgraph_js/examples/02_typescript_durable.ts
 * Expected: parallel findings, a saved approval pause, and an explicit human decision.
 */
import { StateGraph, StateSchema, ReducedValue, Send, Command, interrupt, START, END } from "@langchain/langgraph";
import { SqliteSaver } from "@langchain/langgraph-checkpoint-sqlite";
import { z } from "zod";

export const DEFAULT_CASE = { documents: ["estimate", "receipt"], approved: false };
const State = new StateSchema({
  documents: z.array(z.string()), document: z.string().default(""),
  findings: new ReducedValue(z.array(z.string()).default([]), { reducer: (old, update) => old.concat(update) }),
  approved: z.boolean().default(false),
});

export async function run(input = DEFAULT_CASE) {
  const saver = SqliteSaver.fromConnString(":memory:");
  try {
    const graph = new StateGraph(State)
      .addNode("review_document", (state) => ({ findings: ["reviewed:" + state.document] }))
      .addNode("approve", () => {
        const decision = interrupt({ question: "Approve the synthetic claim?" });
        if (typeof decision !== "boolean") throw new TypeError("Boolean approval required");
        return { approved: true };
      })
      .addConditionalEdges(START, (state) => state.documents.length ? state.documents.map((document) => new Send("review_document", { document })) : ["approve"], ["review_document", "approve"])
      .addEdge("review_document", "approve").addEdge("approve", END).compile({ checkpointer: saver });
    const config = { configurable: { thread_id: "js-claim" } };
    const updates = [];
    for await (const update of await graph.stream({ documents: input.documents, findings: [] }, { ...config, streamMode: "updates" })) updates.push(update);
    const before = await graph.getState(config);
    const value = await graph.invoke(new Command({ resume: input.approved }), config);
    return { findings: [...value.findings].sort(), approved: value.approved, pending_before: before.next, stream_parts: updates.length };
  } finally { saver.db.close(); }
}

async function main() {
  try { console.log(JSON.stringify({ value: await run(process.argv[2] ? JSON.parse(process.argv[2]) : DEFAULT_CASE) })); }
  catch (error) { console.log(JSON.stringify({ error: error instanceof Error ? error.name : "Error" })); }
}
await main();
