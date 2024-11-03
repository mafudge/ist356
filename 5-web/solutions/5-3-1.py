import streamlit as st

from code_helper import run_python_script

st.title("Get Page Content")

url = st.text_input("Enter a URL", "https://ist256.com/fall2023/")
if url:
    with st.spinner("Scraping..."):
        text = run_python_script("5-web/solutions/get-page-text.py", url)
        st.text(text)