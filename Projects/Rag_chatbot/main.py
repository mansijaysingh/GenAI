from dotenv import load_dotenv
import os
import streamlit as st
from rag_pipeline import create_rag_pipeline, ask_questions



load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

st.title("🔥RAG Chatbot")

#chat history store
if "messages" not in st.session_state:
  st.session_state.messages=[]

#Vectore DB store
if "db" not in st.session_state:
  st.session_state.db=None

#Upload file
uploaded_file=st.file_uploader("Upload your PDF📄")

if uploaded_file:
  if st.session_state.db is None:
    with open ("temp.pdf", "wb") as f:
      f.write(uploaded_file.read())

    st.session_state.db = create_rag_pipeline("temp.pdf")
    st.success("PDF Processed✅")

#Show old chat
for msg in st.session_state.messages:

 st.chat_message(msg["role"]).write(msg["content"])

#Input query
query=st.chat_input("Ask something🤗")
if query and st.session_state.db:
  st.session_state.messages.append({"role":"user", "content":query})
  st.chat_message("user").write(query)

  #AI answer
  answer=ask_questions(st.session_state.db,query)
  st.session_state.messages.append({"role": "assistant", "content":answer})
  st.chat_message("assistant").write(answer)




# upload_file=st.file_uploader("Upload Your PDF📁")

# if upload_file:
#   if "db" not in st.session_state:
#    with open("temp.pdf","wb") as f:
#     f.write(upload_file.read())

#    st.session_state.db=create_rag_pipeline("temp.pdf")
#    st.success("PDF Pocessed✅")

#   query=st.text_input("👉Ask Something")

#   if query:
#     answer=ask_questions(st.session_state.db,query)
#     st.write(answer)


