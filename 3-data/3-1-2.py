import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv"
df = pd.read_csv(url,sep=",",header=0)

#always new variable after transform
df_ny = df[ df['State'] == 'NY' ]
df_ny_info = df_ny[['First','Last','Gender','State','Total Purchased']]

st.dataframe(df_ny_info)


