import streamlit as st
from code_helper import run_python_script
import pandas as pd


st.title("Playwright with Streamlit")
st.caption("The strategy is to call the playwright code as a python script")

year = st.number_input("Enter a year", min_value=2010, max_value=2024, value=2023)
if year:
    with st.spinner("Scraping..."):
        html_content = run_python_script("5-web/solutions/5-2-2a.py", str(year))
        df = pd.read_html(html_content)[0]

        st.dataframe(df)

