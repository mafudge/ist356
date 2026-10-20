import streamlit as st
import pandas as pd
import numpy as np
import requests

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"

response = requests.get(url)
json_data = response.json()

employees = pd.json_normalize(json_data, 
                            record_path="employees", 
                              meta=["dept"]
                              ) #<== turn the right nobs

st.dataframe(employees)
