import streamlit as st
import pandas as pd
import numpy as np
import requests

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/json-samples/employees.json"

response = requests.get(url)
data = response.json()

# record_path = 'employees'
# meta = [['department']]
st.write(data)

df = pd.json_normalize(data, record_path='employees', meta=['dept'])
st.dataframe(df)

