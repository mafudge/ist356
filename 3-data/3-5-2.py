import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.title("Exam Scores Pivot Table Example")
#inputs
row = st.multiselect("Select Row", options=list(exams.columns))
col = st.selectbox("Select Column", options=list(exams.columns))
measure = st.selectbox("Select Measure", options=list(exams.columns))
aggregate = st.selectbox("Select Aggregate", options=["mean", "sum", "count"])

try:
    #process
    pivot1 = exams.pivot_table(index=row, columns=col,
                            values=measure, aggfunc=aggregate)
    #output
    st.dataframe(pivot1)

except ValueError as e:
    st.error(f"Row/Column/Measure cannot be re-used. Measures must numbers: {e}")
