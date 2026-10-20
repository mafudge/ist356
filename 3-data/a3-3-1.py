import streamlit as st
import pandas as pd
import requests

url="https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(url)
employees = response.json()

dfs = []
for key in employees.keys():
    df = pd.DataFrame(employees[key]) # make dataframe for key
    df['department'] = key # add a column for the department (lineage)
    dfs.append(df) # add to list of dataframes
combined_df = pd.concat(dfs, ignore_index=True) # combine all dataframes into one

st.dataframe(combined_df) # display the combined dataframe in the app
st.write(employees) # display the original JSON data in the app

