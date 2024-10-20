import streamlit as st  
import requests

url = "http://localhost:8000/tldr"

st.title("AI Text Summarizer")
text = st.text_area("Enter text to summarize")

if st.button("Summarize"):
    with st.spinner("Summarizing..."):
        response = requests.post(url, json={"text": text})
        response.raise_for_status()
        st.write(response.json())