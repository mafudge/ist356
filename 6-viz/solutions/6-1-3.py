import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")

st.dataframe(mobile)

quantity_x = st.selectbox("Select a quantity X", ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "App Usage Time (min/day)", "Screen On Time (hours/day)"])
quantity_y = st.selectbox("Select a quantity Y", ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "App Usage Time (min/day)", "Screen On Time (hours/day)"])

figure, series1 = plt.subplots()
sns.scatterplot(data=mobile, x=quantity_x, y=quantity_y, ax=series1)
st.pyplot(figure)