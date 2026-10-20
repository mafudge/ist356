import streamlit as st
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log"

data = pd.read_csv(url, sep=" ", skiprows=3)

st.dataframe(data)
