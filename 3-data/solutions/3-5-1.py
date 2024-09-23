import streamlit as st
import pandas as pd

st.title("Exam Scores")


options = ['Made_Own_Study_Guide', 'Did_Exam_Prep Assignment', 'Studied_In_Groups']

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

option = st.selectbox('Select Exam:', options)

summary_df = exams.groupby(by=option).agg({'Class_Section': 'count', 'Student_Score' :'mean'})
summary_df = summary_df.rename(columns={'Class_Section': 'Student Count', 'Student_Score': 'Mean Score'})

st.dataframe(summary_df)