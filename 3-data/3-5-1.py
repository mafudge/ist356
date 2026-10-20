import streamlit as st
import pandas as pd

exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.dataframe(exams)
st.write(list(exams.columns))

st.title("Group By Examples")
group1 = exams.groupby(by=['Letter_Grade']).agg({'Letter_Grade': 'count'})
# make letter grade a column instead of an index
group1 = group1.rename(columns={'Letter_Grade': 'Student_Count'})
st.dataframe(group1)

# group by section and exam version and average the scores
group2 = exams.groupby(by=['Class_Section', 'Exam_Version'])\
    .agg({'Student_Score': 'mean', 'Percentage': 'count'})\
    .rename(columns={'Student_Score': 'Average_Score', 'Percentage': 'Student_Count'})

st.dataframe(group2)

st.title("Pivot Table Examples")

pivot1 = exams.pivot_table(index=['Class_Section'],  # ,"Made_Own_Study_Guide"
                           columns=['Exam_Version'], 
                           values='Student_Score', aggfunc='count', fill_value=0)

st.dataframe(pivot1)

st.title("Melt Example:")

melt1 = pivot1.reset_index().melt(id_vars=['Class_Section'], 
                                  var_name='Exam_Version',
                                  value_name='Student_Count')
st.dataframe(melt1)