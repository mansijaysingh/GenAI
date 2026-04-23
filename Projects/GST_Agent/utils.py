import base64
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import pandas as pd
from dotenv import load_dotenv

load_dotenv()


def encode_image(image_path):
  with open (image_path, "rb") as image_file:
    return base64.b64decode(image_file.read()).decode('utf-8')
  

def extract_from_image(file_path):
  model=ChatOpenAI(model="gpt-4o-mini")
  base64_image=encode_image(file_path)

  prompt = """
    You are a professional GST Compliance Expert in India. 
    Analyze the provided invoice image and extract the following details accurately in JSON format:
    
    1. gstin: The GST number of the supplier.
    2. date: The date of the invoice in YYYY-MM-DD format.
    3. total_amount: The grand total amount including taxes (as a float).
    4. tax_amount: The total GST amount (CGST+SGST or IGST) mentioned (as a float).
    5. is_nil_return: Set to true if there are no sales or the invoice represents a zero-rated supply, else false.

    Strict Requirements:
    - Return ONLY the raw JSON object. 
    - Do not include any conversational text, explanations, or markdown formatting (like ```json).
    - If a field is not found, return null for that specific field.
    """
  
  meassage=HumanMessage(
    content=[
      {"type": "text", "text": prompt},
      {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
    ]
  )
  response=model.invoke()
  return response.content


def extract_from_excel(file_path):
  df=pd.read_excel(file_path)
  return df.to_dict(orient="records")

def process_document(file_path):
  ext=os.path.splitext(file_path)
  if ext in ['.jpg', '.jpeg', '.png']:
        return extract_from_image(file_path)
  elif ext in ['.xlsx', '.xls']:
        return extract_from_excel(file_path)
  else:
        return {"error": "It doesn't support"}