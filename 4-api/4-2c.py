import streamlit as st
import dotenv
import pandas as pd
from extract import extract_entities

dotenv.load_dotenv()

st.title("Entity Extraction App")
text = st.text_area("Enter text to extract entities from:", "")    
if st.button("Extract Entities"):
    with st.spinner("Extracting entities..."):
        entities = extract_entities(text)
        df = pd.json_normalize(entities)
        st.dataframe(df)
