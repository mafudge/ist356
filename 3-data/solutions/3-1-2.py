import streamlit as st
import pandas as pd

st.title('My first dataframe')

customers = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv')

radio = st.radio('Show:', options=[ 'Head', 'Tail'], index=0)
rows = st.number_input('Rows:', min_value=1, max_value=len(customers), value=5)
st.write(radio)
if radio == 'Head':
    st.dataframe(customers.head(rows))
else:
    st.dataframe(customers.tail(rows))