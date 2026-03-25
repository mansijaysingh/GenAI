from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client=OpenAI()

SYSTEM_PROMPT="""
  You are an AI persona Assistant named Harshit Sachan.
  You are acting on behalf of Harshit Sachan who is 25 years old content creator and youtuber.

  Examples:
  Q:Hey
  A:Hey,Whats up!
"""

response=client.chat.completions.create(
  model="gpt-4o",
  # response_format={"type":"json_object"},
  messages=[
    {"role":"system", "content":SYSTEM_PROMPT},
    {"role":"user", "content":"Who are you!"}
  ]
)

print(response.choices[0].message.content)