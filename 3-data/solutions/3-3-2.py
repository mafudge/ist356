import streamlit as st
import pandas as pd

base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/minimart/"
months = ['jan', 'feb', 'mar', 'apr']

st.title("Who's not Buying from MiniMart?")
month = st.selectbox('Select Month:', months)

purchases = pd.read_csv(f"{base}/purchases-{month}.csv")
customers = pd.read_csv(f"{base}/customers.csv")
combined = pd.merge(customers, purchases, left_on='customer_id', right_on='customer_id', how='left')
cols = ["customer_id", "firstname", "lastname"]
did_not_buy = combined["order_id"].isnull()
customers_who_did_not_buy = combined[did_not_buy][cols]
st.header("These people ain't buying it!")
st.dataframe(customers_who_did_not_buy, hide_index=True)


st.divider()
st.write("debug")
st.dataframe(combined)