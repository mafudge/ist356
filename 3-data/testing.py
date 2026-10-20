import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/students-header-blanks.csv"

data = pd.read_csv(url, skiprows=5)

st.dataframe(data)
