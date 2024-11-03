import streamlit as st
import pandas as pd
import json
from code_helper import run_python_script


st.title('Craigslist Scraper')
st.caption("Enter a search term to scrape Craigslist I'll return a table of the results.")

search = st.text_input('Enter search term:')

if st.button('Scrape Craigslist'):
    with st.spinner('Scraping Craigslist...'):
        # Run the scraper
        data = run_python_script('5-web/solutions/5-4-1-craigslit-scraper.py', search)
        scraped = json.loads(data)
        df = pd.DataFrame(scraped)
        st.dataframe(df)
        