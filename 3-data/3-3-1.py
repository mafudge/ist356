import streamlit as st
import pandas as pd
import numpy as np
import requests

# use reqests to read in this as json data
url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees-dict.json"
response = requests.get(url)
employee_data = response.json()

# this was me figuring it out...

# st.write(employee_data)

# # loop over each key create a dataframe for each key and display it
# for key in employee_data.keys():
#     st.write(f"Data for {key}:")
#     # emplyee_data[key] gets the value ex 'marketing' this is list
#     df = pd.DataFrame(employee_data[key]) 
#     st.dataframe(df)

dfs = []
for key in employee_data.keys():
    df = pd.DataFrame(employee_data[key])
    df['department'] = key  # add a new column for department (lineage)
    dfs.append(df)

combined_df = pd.concat(dfs, ignore_index=True)
st.write("Combined DataFrame:")
st.dataframe(combined_df)

filename = "3-data/data/combined_employee_data.json"
combined_df.to_json(filename, orient="records", lines=False)
st.write(f"Combined DataFrame saved to '{filename}' in JSON Lines format.")

