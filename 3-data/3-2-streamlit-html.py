import streamlit as st
import pandas as pd

st.title("HTML Example - multiple tables")

contents = pd.read_html("https://web.archive.org/web/20230606035218/https://ist256.com/")

# There are 2 tables on this page, but we don't know this
tables_count = len(contents)

st.write(f"Found {tables_count} tables on the page")

# make tabs for each HTML Table
tab_names = [ f"HTML Table {i}" for i in range(tables_count)]
tabs = st.tabs(tab_names)

# for each tab, show its table
for i in range(len(tabs)):
    df = contents[i]
    tabs[i].dataframe(df)

