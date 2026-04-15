from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph , START, END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


llm=init_chat_model(
  model="gpt-3.5-turbo",
  model_provider="openai"
)




class State(TypedDict):
  message:Annotated[list,add_messages]


def chatbot(state:State):
 response=llm.invoke(state.get("message"))
 return {"message": [response]}

def samplenode(state:State):
  print("\n\nSample node called with state:", state)
  return {"message":["This is a sample node."]}

graph_builder=StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph=graph_builder.compile()

# updated_state=graph.invoke(State({"messages":["Hi, My name is Mansi..."]}))
# print("Updated state after graph execution:", updated_state)

initial_input={"message": ["Hi, My name is Mansi..."]}
updated_state=graph.invoke(initial_input)
print("\n\nUpdated state after graph execution:", updated_state)
