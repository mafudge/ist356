import streamlit as st
import pandas as pd

st.title("Exam Scores Pivot Table")

cols = [ 'Class_Section', 'Exam_Version', 'Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups','Letter_Grade']
measures = ['Student_Score', 'Completion_Time']
exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

row = st.selectbox('Display in Row:', cols)
cols.remove(row)
col = st.selectbox('Display in Column:', cols)
value = st.selectbox('Display Average of:', measures)

pivot_df = exams.pivot_table(index=row, columns=col, values=value, aggfunc='mean')
st.dataframe(pivot_df)