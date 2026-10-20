import streamlit as st
import pandas as pd
from check_functions import clean_currency, detect_whale

# main
checks = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/dining/check-data.csv')

# cleanup currency columns
checks['total_cleaned'] = checks['total amount of check'].apply(clean_currency)
checks['gratuity_cleaned'] = checks.apply( 
    lambda row: clean_currency(row['gratuity']), axis=1)

#calculations 
checks['price_per_item'] = checks['total_cleaned'] / checks['total items on check']
checks['price_per_person'] = checks['total_cleaned'] / checks['party size']
checks['items_per_person'] = checks['total items on check'] / checks['party size']
checks['tip_percentage'] = checks['gratuity_cleaned'] / checks['total_cleaned']

# whale calculations
checks['customer_type'] = checks.apply(
    lambda row: detect_whale(
        row['items_per_person'], 
        row['price_per_person'], 
        checks['items_per_person'].quantile(0.75), 
        checks['price_per_person'].quantile(0.75)), axis=1)

customer_type_counts = checks['customer_type'].value_counts()

columns = st.columns(len(customer_type_counts))

for i, (customer_type, count) in enumerate(customer_type_counts.items()):
    with columns[i]:
        st.metric(label=customer_type, value=count)

st.dataframe(checks)
