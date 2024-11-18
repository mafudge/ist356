import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
pengo = sns.load_dataset("penguins")
pengo['count'] = 1

st.title('Plotly Express Example')
fig = px.bar(pengo, x="species", y="count", color="species", barmode="group")
st.plotly_chart(fig)