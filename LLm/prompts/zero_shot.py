from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

SYSTEM_PROMPT="You are an expert in AI/ML and you only answer related to your field questions. Do not answer anything else. Your name Alexi. If user asks something other than this just say sorry"

response=client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role":"system", "content":SYSTEM_PROMPT},
    {"role":"user", "content":"Hey, can you tell me a joke"}
  ]
)

print(response.choices[0].message.content)
