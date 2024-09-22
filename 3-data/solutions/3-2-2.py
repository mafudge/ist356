import requests
import pandas as pd
import streamlit as st

st.title("Employee JSON")

response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/master/json-samples/employees.json")
employees = response.json()
employees_df = pd.json_normalize(employees, record_path=["employees"], meta=["dept"])
st.dataframe(employees_df)