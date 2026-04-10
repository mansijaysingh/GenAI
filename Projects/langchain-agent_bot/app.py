from langchain_openai import ChatOpenAI
from langchain_classic.agents import initialize_agent
from langchain_classic.tools import Tool
from langchain_classic.memory import ConversationBufferMemory
# from langchain_core.prompts import MessagesPlaceholder
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini")

def calculator(input):
  try:
    return str(eval(input))
  except:
    return "Invalid math expression"

def time_tool(_):
  now = datetime.now()
  return f"Current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

tools=[
  Tool(
    name="Calculator",
    func=calculator,
    description="ONLY use this tool for mathematical calculations. DO NOT use for normal conservations "

  ),
  Tool(
    name="Time",
    func=time_tool,
    description="Use this tool to get the current date and time. DO NOT use for normal conservations"
  )
]

memory=ConversationBufferMemory(
  memory_key='chat_history',
  return_messages=True
)

agent=initialize_agent(
  tools=tools,
  llm=llm,
  agent="chat-conversational-react-description",
  memory=memory,
  handle_parsing_errors=True,
  
  verbose=True
  
)

while True:
  user_input=input("Enter your question: ")

  if user_input == "exit":
    break

  reponse=agent.run(user_input)
  print(f"Agent response: {reponse}")