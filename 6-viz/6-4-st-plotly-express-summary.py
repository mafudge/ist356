
import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Plotly Express Visualizations Example')
st.caption('This is a simple example of how to uses Plotly Express to create visualizations.')
st.caption("Plotly does not aggregate so we must!")

df  = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/delimited/fudge_companies.csv')
st.dataframe(df)

st.write('## Bar Plots')
bar_y = st.selectbox('Select y', ["Ordered", "Returned", "Sold"], key="bar_y")
if bar_y:
    # aggregate with a pivot table
    bar_data = pd.pivot_table(df, values=bar_y, index="Month", aggfunc="sum").reset_index()
    fig = px.bar(bar_data, x="Month", y=bar_y, color="Month",title=f"Total {bar_y} by Month")
    st.plotly_chart(fig)


st.write('## Line Plots')
line_y = st.selectbox('Select y', ["Ordered", "Returned", "Sold"], key="line_y")
if line_y:
    # aggregate with a group by
    line_data = df.groupby("Month")[line_y].mean().reset_index()
    fig = px.line(line_data, x="Month", y=line_y, title=f"Average {line_y} by Month")
    st.plotly_chart(fig)

