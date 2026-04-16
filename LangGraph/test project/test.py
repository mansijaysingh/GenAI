from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm=ChatOpenAI(model="gpt-4o-mini")

class MyState(TypedDict):
  input:str
  output:str


def chatbot(state:MyState):
  response=llm.invoke(state.get("input"))
  return {"output": response.content}

# def calculater(state:MyState):
#   try:
#     result=str(eval(state["input"]))
#   except:
#     result="Invalid math expression"
#   return {"output": result}

def calculater(state: MyState):
    try:
        result = str(eval(state["input"]))
    except:
        result = "Invalid math expression"
    
    return {"output": result}
  
def decide(state: MyState):
    if any(char.isdigit() for char in state["input"]):
        return "calculator"
    return "chatbot"
  

graph_builder=StateGraph(MyState)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("calculator", calculater)

graph_builder.set_conditional_entry_point(decide)

graph_builder.add_edge("chatbot", END)
graph_builder.add_edge("calculator", END)

graph=graph_builder.compile()

while True:
   user_input=input("You:")
   if user_input == "exit":
      break
   result=graph.invoke({"input":user_input})
   print("Bot:", result["output"])