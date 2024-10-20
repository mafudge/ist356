import requests

import streamlit as st

st.title("LLM Crossword Helper")

word = st.text_input("Enter the word")
number = st.number_input("How Many Letters should cross this word? ", min_value=1, max_value=5, value=1)

if st.button("Find Words"):
    with st.spinner("Searching for words..."):
        prompt = f"I am creating a crossword puzzle. I need to {number} other words that cross the word '{word}`. Can you suggest some words?"
        api_key = "GETYOUROWNKEY"
        uri = "https://cent.ischool-iot.net/api/openai/generate"
        data = { "query": prompt }
        response = requests.post(uri, data=data, headers={"x-api-key": api_key})
        response.raise_for_status()
        result = response.json()
        st.write(result)