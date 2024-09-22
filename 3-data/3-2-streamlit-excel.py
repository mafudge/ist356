import streamlit as st
import pandas as pd

st.title("Excel Example - multiple sheets")

contents = pd.read_excel("https://github.com/mafudge/datasets/raw/refs/heads/master/excel-examples/books_of_interest.xlsx", sheet_name=None)

# names of sheets in the excel file its a dictionary
sheets = list(contents.keys()) 

# make tabs for each sheet
tabs = st.tabs(sheets)

#loop through each tab and write the contents of the sheet to the tab
for i in range(len(tabs)):
    df = contents[sheets[i]]
    tabs[i].dataframe(df)

