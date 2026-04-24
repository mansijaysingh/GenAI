from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm=ChatOpenAI(model="gpt-3.5-turbo")


class MyState(TypedDict):
  input:str
  output:str


def chatbot(state:MyState):
  response=llm.invoke(state["input"])
  return {"output":response}

def calculator(state:MyState):
  try:
    result=str(eval(state["input"]))
  except:
    result="invalid expression"
  return {"output":result}


def greeting(state:MyState):
  return {"output":"Hello! How can I assist you today?"}

def decide(state:MyState):
  text=state["input"].lower()
  if any(char.isdigit()for char in text):
    return "calculator"
  elif "hello" in text or "hi" in text:
    return "greeting"
  else:
    return "chatbot"
  

graph_builder=StateGraph(MyState)

#add nodes
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("calculator", calculator)
graph_builder.add_node("greeting", greeting)

graph_builder.set_conditional_entry_point( decide)

graph_builder.add_edge("chatbot", END)
graph_builder.add_edge("calculator", END)
graph_builder.add_edge("greeting", END)

graph=graph_builder.compile()

while True:
  user_input=input("you:")

  if user_input == "exit":
    break

  result=graph.invoke({"input":user_input})
  print("bot:", result["output"])