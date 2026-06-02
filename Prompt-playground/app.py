from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_question= input("Enter your question:")

prompt= f"""
Answer the following question step by step.

Question: {user_question}

"""


response=client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role":"system", "content":"You are a AI tutor"},
    {"role":"user", "content":prompt}
  ]
)


print("\n Answer: \n")
print(response.choices[0].message.content)

