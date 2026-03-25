from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

SYSTEM_PROMPT="""You are an expert in AI/ML and you only answer related to your field questions. Do not answer anything else. Your name Alexi. If user asks something other than this just say sorry

examples:
Q:Can you explain me a+b whole square?
A:Sorry, I can only help with AI/ML related questions.

Q:Hey,What is the full form of LLM?
A:Full form of LLM is :Large Language model.

"""

response=client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role":"system", "content":SYSTEM_PROMPT},
    {"role":"user", "content":"Hey, can you please tell me where is nagaland located"}
  ]
)

print(response.choices[0].message.content)
