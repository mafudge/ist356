import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

row = "Exam_Version"
col = "Studied_In_Groups"
measure = "Completion_Time"

st.title("Universal Pivot Table Example")

row_col_values = ['Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
measure_values = ['Student_Score', 'Completion_Time']
#inputs
row = st.multiselect("Select Row", options=row_col_values)
col = st.selectbox("Select Column", options=row_col_values)
measure = st.selectbox("Select Measure", options=measure_values)

#procees
try:
    pivot1 = exams.pivot_table(
        index=row, columns=col, values=measure, aggfunc='mean')

    # outputs
    st.write(f"Pivot Table: `{row}` x `{col}` with `{measure}` as mean")
    st.dataframe(pivot1)

except ValueError as e:
    st.error(f"Row and column must not use the same value. Error: {e}")
