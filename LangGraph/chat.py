from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph , START, END



class State(TypedDict):
  message:Annotated[list,add_messages]


def chatbot(state:State):
  print("Chatbot node called with state:", state)
  return {"messages":["Hi! How can I help you?"]}

def samplenode(state:State):
  print("Sample node called with state:", state)

  return {"messages":["This is a sample node."]}

graph_builder=StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph=graph_builder.compile()


