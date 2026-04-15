from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph



class State(TypedDict):
  message:Annotated[list,add_messages]


def chatbot(state:State):

  return {"messages":["Hi! How can I help you?"]}

def samplenode(state:State):

  return {"messages":["This is a sample node."]}

graph_builder=StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)


