import requests
import streamlit as st

st.title("LLM Spell Checker")

text = st.text_area("Enter your text:")

if st.button("Spell Check"):
    with st.spinner("Searching misspellings..."):
        prompt = f'''
        Can your check the following text for spelling errors?
        For each misspelled word, please output the word and one suggested correct spelling.
        Text to check for spelling errors:
     
        {text}
        '''
        api_key = "ea044c96950db6cc0fab7ae1"
        uri = "https://cent.ischool-iot.net/api/openai/generate"
        data = { "query": prompt }
        response = requests.post(uri, data=data, headers={"x-api-key": api_key})
        response.raise_for_status()
        result = response.json()
        st.write(result)