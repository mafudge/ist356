import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
pengo = sns.load_dataset("penguins")
pengo['count'] = 1

st.dataframe(pengo)

figure, series1 = plt.subplots()
sns.barplot(data=pengo, x="sex", y="body_mass_g", hue="sex", estimator="mean", ax=series1)
st.pyplot(figure)

figure, series1 = plt.subplots()
sns.barplot(data=pengo, x="sex", y="body_mass_g", hue="sex", estimator="mean", errorbar=None, ax=series1)
st.pyplot(figure)

