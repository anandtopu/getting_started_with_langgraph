// YOUR CODE HERE: repair the task contract.
/** Compare a wired tool loop with createAgent using the same fake trajectory. No live model.
 * Run: node modules/bonus/B1_langgraph_js/examples/03_typescript_agents.ts
 * Expected: human -> AI request -> tool response -> AI conclusion in both implementations.
 */
import { StateGraph, StateSchema, MessagesValue, START, END } from "@langchain/langgraph";
import { ToolNode } from "@langchain/langgraph/prebuilt";
import { AIMessage, HumanMessage, ToolMessage } from "@langchain/core/messages";
import { tool } from "@langchain/core/tools";
import { createAgent } from "langchain";
import { z } from "zod";
import { getChatModel } from "#course/models";

export const DEFAULT_CASE = { policy_id: "POL-0001", recursion_limit: 12 };
const lookup = tool(({ policy_id }) => {
  if (policy_id !== "POL-0001") throw new Error("Unknown synthetic policy");
  return "Deductible: 100000 cents";
}, { name: "lookup_policy", description: "Read a synthetic deductible", schema: z.object({ policy_id: z.string() }) });
const State = new StateSchema({ messages: MessagesValue });

export async function run(input = DEFAULT_CASE) {
  function model() {
    return getChatModel([
      new AIMessage({ content: "", tool_calls: [{ name: "lookup_policy", args: { policy_id: input.policy_id }, id: "lookup-1", type: "tool_call" }] }),
      new AIMessage("Policy evidence checked; no payment authorized."),
    ]);
  }
  const fake = model().bindTools([lookup]);
  const manual = new StateGraph(State)
    .addNode("model", async (state) => ({ messages: [await fake.invoke(state.messages)] }))
    .addNode("tools", new ToolNode([lookup]))
    .addEdge(START, "model")
    .addConditionalEdges("model", (state) => {
      const last = state.messages.at(-1);
      return AIMessage.isInstance(last) && last.tool_calls?.length ? "tools" : END;
    }, ["tools", END]).addEdge("tools", "model").compile();
  const inputState = { messages: [new HumanMessage("Check the deductible.")] };
  const config = { recursionLimit: input.recursion_limit };
  const first = await manual.invoke(inputState, config);
  const second = await createAgent({ model: model(), tools: [] }).invoke(inputState, config);
  const roles = first.messages.map((message) => message.type);
  return { roles, prebuilt_roles: second.messages.map((message) => message.type), final: first.messages.at(-1)?.content,
    tool_ids: first.messages.filter(ToolMessage.isInstance).map((message) => message.tool_call_id) };
}

async function main() {
  try { console.log(JSON.stringify({ value: await run(process.argv[2] ? JSON.parse(process.argv[2]) : DEFAULT_CASE) })); }
  catch (error) { console.log(JSON.stringify({ error: error instanceof Error ? error.name : "Error" })); }
}
await main();
