from dotenv import load_dotenv
import os
import streamlit as st
from rag_pipeline import create_rag_pipeline, ask_questions



load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

st.title("🔥RAG Chatbot")

upload_file=st.file_uploader("Upload Your PDF📁")

if upload_file:
  if "db" not in st.session_state:
   with open("temp.pdf","wb") as f:
    f.write(upload_file.read())

   st.session_state.db=create_rag_pipeline("temp.pdf")
   st.success("PDF Pocessed✅")

  query=st.text_input("👉Ask Something")

  if query:
    answer=ask_questions(st.session_state.db,query)
    st.write(answer)


