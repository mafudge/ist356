import streamlit as st
import pandas as pd

st.title('Customers')
customers = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv')
radio = st.radio('Gender:', options=[ 'M', 'F'], index=0)
cols = st.multiselect('Columns:', options=customers.columns)
gender_index = customers['Gender'] == radio
st.dataframe(customers[gender_index][cols])