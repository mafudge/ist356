import requests
import json
import pandas as pd 
import streamlit as st

st.title("LLM Spell Checker v2")

text = st.text_area("Enter your text:")

if st.button("Spell Check"):
    with st.spinner("Searching misspellings..."):
        prompt = '''
        I would like you to check input text for spelling errors, suggest corrections, and output the corrected text.
        
        Output must be in a machine-readable format. 
        EXAMPLE 1
        {
            "text": "trhis is a test",
            "corrected-text" : "this is a test",
            "corrections": [
                {
                    "word": "trhis",
                    "correction": "this"
                }
            ]
        }


        EXAMPLE 2
        {
            "text": "I lyke cheez!",
            "corrected-text" : "I like cheese!",
            "corrections": [
                {
                    "word": "lyke",
                    "correction": "like"
                },
                {
                    "word": "cheez",
                    "correction": "cheese"
                }
            ]
        }
        
        Here is the Text to check for spelling errors:
     
        '''
        prompt += text

        api_key = "ea044c96950db6cc0fab7ae1"
        uri = "https://cent.ischool-iot.net/api/openai/generate"
        data = { "query": prompt }
        response = requests.post(uri, data=data, headers={"x-api-key": api_key})
        response.raise_for_status()
        result = response.json()
        json_result = json.loads(result)
        st.write(json_result)
        st.write("CORRECTED TEXT:")
        st.write(json_result['corrected-text'])
        df = pd.DataFrame(json_result['corrections'])
        st.write("CORRECTIONS:")
        st.dataframe(df)