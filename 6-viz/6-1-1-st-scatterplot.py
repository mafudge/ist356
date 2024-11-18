import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
pengo = sns.load_dataset("penguins")
pengo['count'] = 1

plot, series = plt.subplots()
sns.scatterplot(data=pengo, x="bill_length_mm", y="bill_depth_mm", hue="species", ax=series).set_title("Bill Length vs Bill Depth")
st.pyplot(plot)