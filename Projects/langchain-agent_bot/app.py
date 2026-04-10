from langchain_openai import ChatOpenAI
from langchain_classic.agents import initialize_agent
from langchain_classic.agents import AgentExecutor
from langchain_classic.tools import Tool
from langchain_classic.memory import ConversationBufferMemory
from dotenv import load_dotenv
import datetime

load_dotenv()

llm=ChatOpenAI()

def calculator(input):
  return str(eval(input))

tools=[
  Tool(
    name="Calculator",
    func=calculator,
    description="Useful for when you need to answer questions about math. Input should be a valid mathematical expression."

  )
]

memory=ConversationBufferMemory()

agent=initialize_agent(
  tools,
  llm,
  agent="openai-functions",
  memory=memory,
  verbose=True,
  handle_parsing_errors=True
)

while True:
  user_input=input("Enter your question: ")

  if user_input == "exit":
    break

  reponse=agent.run(user_input)
  print(f"Agent response: {reponse}")