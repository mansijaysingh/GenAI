from dotenv import load_dotenv
import os
import streamlit as st
from rag_pipeline import create_rag_pipeline, ask_question



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
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file is not None:
    # 👉 file change detect karne ke liye
    if "last_uploaded" not in st.session_state or st.session_state.last_uploaded != uploaded_file.name:
        
        # 🔥 RESET EVERYTHING
        st.session_state.messages = []
        st.session_state.db = None

        import shutil
        import os
        if os.path.exists("faiss_db"):
            shutil.rmtree("faiss_db")

        # 👉 new file save
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())

        # 👉 new DB create
        st.session_state.db = create_rag_pipeline("temp.pdf")

        st.session_state.last_uploaded = uploaded_file.name

        st.success("New PDF processed ✅")
#Show old chat
for msg in st.session_state.messages:

 st.chat_message(msg["role"]).write(msg["content"])

#Input query
query=st.chat_input("Ask something🤗")
if query and st.session_state.db:
  st.session_state.messages.append({"role":"user", "content":query})
  st.chat_message("user").write(query)

  #AI answer
  chat_history = ""
  for msg in st.session_state.messages[-3:]:
     chat_history += f"{msg['role']}: {msg['content']}\n"

  final_query = f"""
  Chat History:
  {chat_history}

  Current Question:
  {query}
"""

  answer = ask_question(st.session_state.db, final_query)
  
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


