import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
pengo = sns.load_dataset("penguins")
pengo['count'] = 1

st.dataframe(pengo)
figure, series1 = plt.subplots()
sns.barplot(data=pengo, x="species", y="count", hue="species", estimator="sum", ax=series1).set_title("Total Count by Species")
st.pyplot(figure)
