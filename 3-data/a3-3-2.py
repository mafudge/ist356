import streamlit as st
import pandas as pd

base_url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"

months = ['jan', 'feb', 'mar', 'apr']
select_month = st.radio("Select a month:", months, horizontal=True)

# process
url = base_url + f"purchases-{select_month}.csv"
df = pd.read_csv(url)
df['month'] = select_month
customer_url = base_url + f"customers.csv"
customer_df = pd.read_csv(customer_url)
combined = pd.merge(df, customer_df,
                    left_on='customer_id', right_on='customer_id', 
                    how='right')

# filter combined where order_id is null
combined_no_orders = combined[combined['order_id'].isnull()]

# project only the columns we want to see and make a new dataframe
combined_no_orders_cols = combined_no_orders[['customer_id', 'firstname', 'lastname']]

# output
st.dataframe(combined_no_orders_cols)

file = '3-data/data/extract.jsonl'
combined_no_orders_cols.to_json(file, orient='records', lines=True)