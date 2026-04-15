from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini", 
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "what's in this image?"}, 
        {
          "type": "image_url",
          "image_url": {
            "url": "https://images.pexels.com/photos/8694473/pexels-photo-8694473.jpeg" 
          }
        }
      ]
    }
  ]
)

print("Response:", response.choices[0].message.content)