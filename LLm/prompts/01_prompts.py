from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

response=client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role":"system", "content":"You are an expert in AI/ML and you only answer related to your field questions"},
    {"role":"user", "content":"Hey, can you explain me how can i become An AI engineer"}
  ]
)

print(response.choices[0].message.content)
