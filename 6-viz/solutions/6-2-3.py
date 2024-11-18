import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ff = pd.read_csv("./6-viz/data/fast_food_nutrition_cleaned.csv")
print(ff.columns)

companies = sorted(list(ff['company'].unique()))
print(companies)

value = st.selectbox("Select Macronutrient", ['fat_g', 'carbs_g', 'sugars_g', 'protein_g', 'sodium_mg'])

ffp = ff.pivot_table(index='company', columns='calories',values=value, aggfunc=np.mean)

figure, series1 = plt.subplots()
sns.heatmap(ffp, ax=series1)
st.pyplot(figure)

