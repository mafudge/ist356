import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/chipolte/orders.tsv"
url2= "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-no-header.csv"
url3 = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-header-blanks.csv"
order = pd.read_csv(url3, sep=",", skiprows= 5)
st.dataframe(order)



col1 = [ "A","B","C","D"]
col2 = [ "B", "C", "A", "D"]
same = s