from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()


SYSTEM_PROMPT="""
    You are an expert Ai assistance in resolving user quaries using chain of thought.
    you work on START, PLAN and OUTPUT steps.
    you need to first PLAN what needs to be done. the PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.


    Rules:
    -Strictly follow given JSON output format
    -Only run one step at a time.
    -The sequence of steps is START (where user gives an input ), PLAN(that can be multiple times) and finallt OUTPUT(which is going to the displayed to the user).

    Output JSON format:
    {"step":"START |"PLAN" | "OUTPUT", "content":"string"}

    example:
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
"""

response=client.chat.completions.create(
  model="gpt-4o-mini",
  response_format={"type":"json_object"},
  messages=[
    {"role":"system", "content":SYSTEM_PROMPT},
    {"role":"user", "content":"Hey, write a code to add n numbers is javascript"}
  ]
)



print(response.choices[0].message.content)