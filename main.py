from datetime import datetime
import json
from langchain_core.tools import tool
from langgraph.graph import StateGraph, END
from langchain_ollama import OllamaLLM
from typing import TypedDict, List, Annotated
import operator


@tool
def get_current_time() -> dict:
    """Return the current UTC time in ISO-8601 format.
    Example → {"utc": "2025-05-25T08:13:00Z"}"""
    return {"utc": datetime.utcnow().isoformat() + "Z"}


llm = OllamaLLM(model="llama3.2")


class State(TypedDict):
    messages: Annotated[List[dict], operator.add]


def chat_node(state: State):
    messages = state["messages"]
    last_message = messages[-1]["content"]

    if "time" in last_message.lower():
        tool_result = get_current_time.invoke({})
        return {"messages": [{"role": "assistant", "content": json.dumps(tool_result)}]}

    response = llm.invoke(last_message)
    return {"messages": [{"role": "assistant", "content": response}]}


workflow = StateGraph(State)

workflow.add_node("chat", chat_node)

workflow.set_entry_point("chat")

workflow.add_edge("chat", END)

app = workflow.compile()


def main():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        state = {"messages": [{"role": "user", "content": user_input}]}
        result = app.invoke(state)
        print("Bot:", result["messages"][-1]["content"])


if __name__ == "__main__":
    main()
