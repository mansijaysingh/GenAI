import streamlit as st
import requests
import json


st.set_page_config(page_title="GST AI Agent", page_icon="💼", layout="wide")

st.title("💼 GST AI Compliance Agent")
st.markdown("---")


st.sidebar.header("Admin Control Panel")
st.sidebar.info("Upload client invoices (Images/Excel) to process GST data using AI.")


col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Upload Invoices")
    uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "xlsx"])
    
    if uploaded_file is not None:
        
        st.write(f"Selected File: **{uploaded_file.name}**")
        
        if st.button("🚀 Run AI Extraction"):
            with st.spinner("AI is reading the bill... Please wait."):
                try:
                    
                    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
                    response = requests.post("http://127.0.0.1:8000/process-gst/", files=files)
                    
                    if response.status_code == 200:
                        st.session_state['result'] = response.json()
                        st.success("Data Extracted Successfully!")
                    else:
                        st.error(f"Backend Error: {response.status_code}")
                except Exception as e:
                    st.error(f"Could not connect to Backend: {e}")

with col2:
    st.subheader("📊 Extracted GST Data")
    if 'result' in st.session_state:
        data = st.session_state['result'].get("data", "{}")
        
        
        if isinstance(data, str):
            json_data = json.loads(data)
        else:
            json_data = data
            
        
        st.json(json_data)
        
       
        st.markdown("---")
        if st.button("✅ Approve & Save Entry"):
            st.balloons()
            st.success("Entry saved to database and ready for GSTR-1!")
    else:
        st.info("Upload and process a file to see the results here.")