from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()
client=OpenAI()

question=input("Ask Something:")

response=client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"user", "content":question}])

print("\nAI Response:\n")
print(response.choices[0].message.content)