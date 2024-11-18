import streamlit as st
import pandas as pd

st.title('Streamlit Plotting Example')
st.caption('This is a simple example of how to use Streamlit to create visualizations')


df  = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/delimited/fudge_companies.csv')
st.dataframe(df)

st.write('## Bar Chart')
st.caption("Aggregates data,, auto sum...")
bar_y = st.selectbox('Select y', ["Ordered", "Returned", "Sold"])
if bar_y:
    st.plotly_chart(df, x = "Month", y= "Sold")


st.write('## Line. Area, Scatter Charts')
st.caption("Does not aggregate, must be row level...")
line_store = st.selectbox('Select Store', ["Mikeazon", "Fudgemart"])
line_dept = st.selectbox('Select Dept', ["Doodads", "Niknaks", "Widgets"])
if line_store and line_dept:
    line_data = df[(df['Store'] == line_store)&(df['Dept'] == line_dept)]
    st.write("###", line_store, line_dept)
    st.line_chart(line_data, x = "Month", y= ["Ordered", "Returned", "Sold"])
    st.area_chart(line_data, x = "Month", y= ["Ordered", "Returned", "Sold"])
    st.scatter_chart(line_data, x = "Ordered", y = "Sold")


