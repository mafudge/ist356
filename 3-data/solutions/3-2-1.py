import pandas as pd
import streamlit as st

st.title("Webtraffic Data")

wt = pd.read_csv("https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log", skiprows=3, header=0, sep="\s+")
wt.info() # colunmn info (to console only)

wt_filter = (wt['sc-status'] == 200) & ( wt['time-taken'] > 500)
wt_slow_but_successful = wt[wt_filter]
st.dataframe(wt_slow_but_successful) # first 20 rows

