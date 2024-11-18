import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

mobile = pd.read_csv("./6-viz/data/mobile_user_behavior_dataset.csv")

st.dataframe(mobile)

category = st.selectbox("Select a category", ["Gender", "Operating System"])
quantity = st.selectbox("Select a quantity", ["Data Usage (MB/day)", "Battery Drain (mAh/day)", "App Usage Time (min/day)", "Screen On Time (hours/day)"])

figure, series1 = plt.subplots()
sns.barplot(data=mobile, x=category, y=quantity, estimator="mean", ax=series1).set_title(f"Total {quantity} by {category}")
st.pyplot(figure)