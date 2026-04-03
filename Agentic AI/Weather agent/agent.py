from openai import OpenAI
from dotenv import load_dotenv
import json
import requests

load_dotenv()

client=OpenAI()

def get_weather(city:str):
  url=f"https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true"
  response=requests.get(url)

  if response.status_code==200:
    return (f"The weather in {city} is {response.json()}")
  
  return "Something went wrong"


available_tools={
  "get_weather": get_weather

}



SYSTEM_PROMPT="""
    You are an expert Ai assistance in resolving user quaries using chain of thought.
    you work on START, PLAN and OUTPUT steps.
    you need to first PLAN what needs to be done. the PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    you can also call a tool if required from the list of available tools.
    for every tool call wait for the observe the steps which is the output from the called tool.


    Rules:
    -Strictly follow given JSON output format
    -Only run one step at a time.
    -The sequence of steps is START (where user gives an input ), PLAN(that can be multiple times) and finallt OUTPUT(which is going to the displayed to the user).

    Output JSON format:
    {"step":"START |"PLAN" | "OUTPUT" |"TOOL", "content":"string", "tool": "string", "input":"string"}

    Available tools:
    -get_weather(city:str): gives the current weather of the city

    example 1:
    START: Can you solve 2+3*5/10
    PLAN:{"step":"PLAN": "content": "seems like user is interesed in math problem"}
    PLAN:{"step":"PLAN": "content": "looking at the problem, we should solve this using BODMAS method"}
    PLAN:{"step":"PLAN": "content": "Yes, the BODMAS is correct thing to be done here"}
    PLAN:{"step":"PLAN": "content": "first we must multiply 3*5 which is 15"}
    PLAN:{"step":"PLAN": "content": "Now the equation is 2+15/10"}
    PLAN:{"step":"PLAN": "content": "we must perform  divide that is 15/10 =1.5"}
    PLAN:{"step":"PLAN": "content": "Now the new equation is 2+1.5"}
    PLAN:{"step":"PLAN": "content": "Now finally lets perform the addition 3.5"}
    PLAN:{"step":"PLAN": "content": "Great, we have solved and left with 305 as answer"}
    PLAN:{"step":"OUTPUT": "content": "3.5"}

    example 2:
    START: What is the weather of delhi?
    PLAN:{"step":"PLAN": "content": "User is interested in knowing the weather of delhi"}
    PLAN:{"step":"PLAN": "content": "Lets see if we  have any avaible tool from the list of available tools that can be used to get the weather"}
    PLAN:{"step":"PLAN": "content": "Great we have get_weather tool  availble for this query"}
    PLAN:{"step":"PLAN": "content": "I need to call the tool get_weather with city name delhi"}
    PLAN:{"step":"TOOL": "tool": "get_weather", "content": "Delhi"}
    PLAN:{"step":"OBSERVER":"tool": "get_weather", "output": "The weather in Delhi is {weather}"}
    PLAN:{"step":"PLAN": "content": "Great I got the weather info about delhi"}
    PLAN:{"step":"OUTPUT": "content": "The weather in Delhi is {weather}"}
"""
print("\n\n\n")

message_history=[
  {"role":"system", "content":SYSTEM_PROMPT},
]

user_query=input("👉")
message_history.append({"role":"user", "content":user_query})

while True:
  response=client.chat.completions.create(
  model="gpt-4o-mini",
  response_format={"type":"json_object"},
  messages=message_history
  )

  raw_result=(response.choices[0].message.content)
  message_history.append({"role":"assistant","content":raw_result})
  parsed_result=json.loads(raw_result)
  if parsed_result.get("step")=="START":
   print("🔥",parsed_result.get("content"))
   continue

  if parsed_result.get("step")=="TOOL":
    tool_to_call=parsed_result.get("tool")
    tool_input=parsed_result.get("input")
    print("🔧 Calling tool",tool_to_call,"with input",tool_input)


    tool_result=available_tools[tool_to_call](tool_input)
    print("🔧 Calling tool",tool_to_call,"with input",tool_input ,tool_result)
    message_history.append({"role":"developer", "content":json.dumps({
      "step":"OBSERVER",
      "tool":tool_to_call,
      "input":tool_input,
      "output":tool_result
    })})
    continue

  if parsed_result.get("step")=="PLAN":
   print("🧠",parsed_result.get("content"))
   continue

  if parsed_result.get("step")=="OUTPUT":
   print("🤖",parsed_result.get("content"))
   break




print("\n\n\n")


# response=client.chat.completions.create(
#   model="gpt-4o-mini",
#   response_format={"type":"json_object"},
#   messages=[
   
#     {"role":"user", "content":"Hey, write a code to add n numbers is javascript"}
#   ]
# )



# print(response.choices[0].message.content)