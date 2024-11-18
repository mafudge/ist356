import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ff = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
print(ff.columns)

companies = sorted(list(ff['company'].unique()))
print(companies)

c1 = st.selectbox("Select Company 1", companies)
c2 = st.selectbox("Select Company 2", companies)

ff_filtered = ff[(ff['company'] == c1) | (ff['company'] == c2)]

figure, series1 = plt.subplots()
figure = sns.lmplot(data=ff_filtered, x="calories", y='sodium_mg', hue='company')
st.pyplot(figure)

st.dataframe(ff_filtered)
