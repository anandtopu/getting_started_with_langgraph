// YOUR CODE HERE: repair the task contract.
/** Typed state, partial updates, and reducers. Run: node modules/bonus/B1_langgraph_js/examples/01_typescript_state.ts
 * No LLM. Expected: trim the description, route integer cents, retain both audit labels.
 */
import { StateGraph, StateSchema, ReducedValue, START, END } from "@langchain/langgraph";
import { z } from "zod";

export const DEFAULT_CASE = { claim_id: "CLM-0001", description: "  Pipe burst  ", amount_cents: 125000 };
const State = new StateSchema({
  claim_id: z.string(), description: z.string(), amount_cents: z.number().int().nonnegative(),
  route: z.string().default(""),
  audit: new ReducedValue(z.array(z.string()).default([]), { reducer: (old, update) => old.concat(update) }),
});

export async function run(input = DEFAULT_CASE) {
  const graph = new StateGraph(State)
    .addNode("normalize", (state) => ({ description: state.description.trim(), audit: ["normalized"] }))
    .addNode("assign_route", (state) => ({ route: !state.description ? "needs_information" : state.amount_cents < 100000 ? "fast_track" : "standard", audit: ["routed"] }))
    .addEdge(START, "normalize").addEdge("normalize", "assign_route").addEdge("assign_route", END).compile();
  return await graph.invoke({ ...input, audit: [] });
}

async function main() {
  try { console.log(JSON.stringify({ value: await run(process.argv[2] ? JSON.parse(process.argv[2]) : DEFAULT_CASE) })); }
  catch (error) { console.log(JSON.stringify({ error: error instanceof Error ? error.name : "Error" })); }
}
await main();
