import streamlit as st
import pandas as pd
import numpy as np

# inputs and get url's
base="https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ["jan", "feb", "mar", "apr"]
selected = st.selectbox("Select a month", months)
monthly_url= f"{base}purchases-{selected}.csv"
customers_url= f"{base}customers.csv"

#dataframes and merges
orders = pd.read_csv(monthly_url)
customers = pd.read_csv(customers_url)
combined = pd.merge(orders, customers, 
                    left_on='customer_id', 
                    right_on='customer_id',
                    how='right')

# slight manipulation to make the data more accurate
combined_filtered = combined[combined['order_id'].isnull()]
combined_filtered_cols = combined_filtered[
    ['customer_id', 'firstname', 'lastname']
]
#outputs
st.dataframe(combined_filtered_cols)


