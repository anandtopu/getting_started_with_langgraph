/** The sole model factory for the TypeScript lessons; scripts are deterministic and offline. */
import { FakeListChatModel } from "@langchain/core/utils/testing";
import { AIMessage, type BaseMessage } from "@langchain/core/messages";
import type { ChatResult } from "@langchain/core/outputs";

class ScriptedChatModel extends FakeListChatModel {
  script: AIMessage[];
  position = 0;
  constructor(script: AIMessage[]) {
    super({ responses: ["scripted"], disableStreaming: true });
    this.script = script;
  }
  override async _generate(_messages: BaseMessage[]): Promise<ChatResult> {
    const message = this.script[this.position++];
    if (!message) throw new Error("Scripted model exhausted its responses");
    return { generations: [{ message, text: typeof message.content === "string" ? message.content : "" }] };
  }
  override bindTools(_tools: Parameters<FakeListChatModel["bindTools"]>[0]): ReturnType<FakeListChatModel["bindTools"]> {
    // Keep this instance: a fake that clones a base model would lose the scripted tool calls.
    return this.withConfig({}) as ReturnType<FakeListChatModel["bindTools"]>;
  }
}

export function getChatModel(responses: AIMessage[]): ScriptedChatModel {
  return new ScriptedChatModel(responses);
}
