import requests
import pandas as pd
import streamlit as st

st.title('API Example API to Pandas')

uri = "https://jsonplaceholder.typicode.com/users/"
response = requests.get(uri)
response.raise_for_status()
data = response.json()
df = pd.json_normalize(data)
st.dataframe(df)
