import streamlit as st

st.title("🤖 My AI Assistant")
user_input=st.text_input("Ask Something:")

if user_input:
    st.write("You:", user_input)
