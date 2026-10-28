import os
import pandas as pd
import requests 
import streamlit as st
import dotenv

dotenv.load_dotenv()

CENT_API_KEY = os.getenv("CENT_API_KEY")

def query_it(df : pd.DataFrame, question: str) -> str:
    '''
    Use genative AI to answer a question about a dataframe. 
    The dataframe is converted to a string and sent to the API along with the question. 
    The API returns a response which is then returned by this function.
    '''

    prompt = f"""
        With the following data:
        {df.to_string(index=False)}
        Answer the following question:
        {question}
    """ 

    url = "https://portal.app.cent-su.org/api/azure/foundry/generate"
    params = { "model": "gpt-6-luna", "max_tokens": 128000, "reasoning_effort": "high", "cache": True }
    response = requests.post(url, data={"query": prompt}, headers={"x-api-key" : CENT_API_KEY}, params=params)
    response.raise_for_status()
    results = response.json()
    return results

st.title("Query It!")
st.caption("Ask a question of your data. Benefits of large context windows.")

file = st.file_uploader("Upload a csv file", type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)

    question = st.text_area("What question would you like to ask of this data?")
    if question:
        with st.spinner("Querying..."):
            try:
                results = query_it(df, question)
                st.write(results)
            except Exception as e:
                st.error(f"An error occurred: {e}")