import streamlit as st
import pandas as pd
from check_functions import clean_currency, detect_whale, detect_tipper

st.title("Dining Check Data")

#load
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')

#transoformations
checks['total_amount_of_check_cleaned'] = checks['total amount of check'].apply(clean_currency)
checks['gratuity_cleaned'] = checks['gratuity'].apply(clean_currency)
checks['price_per_item'] = checks['total_amount_of_check_cleaned'] / checks['total items on check']
checks['price_per_person'] = checks['total_amount_of_check_cleaned'] / checks['party size']
checks['items_per_person'] = checks['total items on check'] / checks['party size']
checks['tip_percentage'] = checks['gratuity_cleaned'] / checks['total_amount_of_check_cleaned']

# Get KPI boundaries:
ppp_75 = checks['price_per_person'].quantile(0.75)
ipp_75 = checks['items_per_person'].quantile(0.75)
tp_75 = checks['tip_percentage'].quantile(0.75)
tp_25 = checks['tip_percentage'].quantile(0.25)

# Calcualte KPI's
checks['whale'] = checks.apply(lambda row: detect_whale(row['items_per_person'], row['price_per_person'], ipp_75, ppp_75), axis=1)
checks['tipper'] = checks.apply(lambda row: detect_tipper(row['tip_percentage'], tp_75, tp_25), axis=1)


st.dataframe(checks, width=1000)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Average Price Per Item", checks['price_per_item'].mean())
col2.metric("Average Price Per Person", checks['price_per_person'].mean())
col3.metric("Average Items Per Person", checks['items_per_person'].mean())
col4.metric("Average Tip Pct", checks['tip_percentage'].mean())

st.dataframe(checks.describe())