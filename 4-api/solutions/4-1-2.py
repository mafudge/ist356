import requests
import pandas as pd
import streamlit as st


st.title("Funny Name Search")

uri = "https://cent.ischool-iot.net/api/funnyname/search"
search = st.text_input("Search for a funny name")
if st.button("Search"):
    response = requests.get(uri, params={"q": search})
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)