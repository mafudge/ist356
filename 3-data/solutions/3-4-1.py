import streamlit as st
import pandas as pd
from check_functions import clean_currency, detect_whale

st.title("Dining Check Data")

# load
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')

# transformations
checks['total_amount_of_check_cleaned'] = checks['total amount of check'].apply(clean_currency)
checks['gratuity_cleaned'] = checks['gratuity'].apply(clean_currency)
checks['price_per_item'] = checks['total_amount_of_check_cleaned'] / checks['total items on check']
checks['price_per_person'] = checks['total_amount_of_check_cleaned'] / checks['party size']
checks['items_per_person'] = checks['total items on check'] / checks['party size']
checks['tip_percentage'] = checks['gratuity_cleaned'] / checks['total_amount_of_check_cleaned']

st.dataframe(checks, width=1000)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Average Price Per Item", checks['price_per_item'].mean())
col2.metric("Average Price Per Person", checks['price_per_person'].mean())
col3.metric("Average Items Per Person", checks['items_per_person'].mean())
col4.metric("Average Tip Pct", checks['tip_percentage'].mean())

st.dataframe(checks.describe())