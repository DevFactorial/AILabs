from langgraph.graph import StateGraph, MessagesState, START, END
from typing import TypedDict, Literal, Callable, Dict, Any, Optional
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode
from langchain_core.messages import AIMessage, HumanMessage
from app.core.tools import get_food_by_nutrients

model_name = "llama-3.2-90b-vision-preview"
tools = [get_food_by_nutrients]
tool_node = ToolNode(tools)

model_with_tools = ChatGroq(
        model = model_name,
        temperature = 1.0,
        max_tokens = 3000,
        timeout = None
        # other params...
    ).bind_tools(tools)

def should_continue(state: MessagesState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END

def call_model(state: MessagesState):
    messages = state["messages"]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}

def execute_agent(input):
    workflow = StateGraph(MessagesState)

    # Define the two nodes we will cycle between
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", tool_node)

    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", should_continue, ["tools", END])
    workflow.add_edge("tools", "agent")

    app = workflow.compile()
    for chunk, metadata in app.stream(
        {"messages": [("human", input)]}, stream_mode="messages"
    ):
         
         if (
            chunk.content
            and isinstance(chunk, AIMessage) 
        ):
            print('content')
            print(chunk)
            print(chunk.content)
            yield chunk.content