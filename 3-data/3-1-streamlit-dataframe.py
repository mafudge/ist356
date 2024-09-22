import streamlit as st
import pandas as pd

st.title("Dataframe Example")

customers = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv")

st.dataframe(customers.head(20))
st.dataframe(customers.describe())