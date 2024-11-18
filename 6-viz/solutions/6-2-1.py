import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# data needs to be cleaned up :-( not uncommon
ff = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
print(ff.columns)

bins = st.slider("Bins", min_value=1, max_value=100)
st.write(f"Number of bins: {bins}")
figure, series1 = plt.subplots()
sns.histplot(data=ff, x="calories", bins=bins, kde=True, ax=series1)
st.pyplot(figure)

st.dataframe(ff)
print(ff.info())