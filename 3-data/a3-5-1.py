import streamlit as st
import pandas as pd


exams = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/exam-scores/exam-scores.csv')

st.write(list(exams.columns))
st.dataframe(exams)

exams_by_section = exams.groupby(by=['Class_Section'])\
    .agg({ 'Class_Section': 'count', 'Student_Score': 'mean' })

st.dataframe(exams_by_section)

exams_counts_by_section_and_version = \
    exams.groupby(by=['Class_Section', 'Exam_Version'])\
    .agg({ 'Student_Score': 'count' })
# common problem need to rename Student_Score to something else, 
# otherwise it will be confusing
exams_counts_by_section_and_version = \
    exams_counts_by_section_and_version.\
        rename(columns={'Student_Score': 'Count_of_Students'})

st.dataframe(exams_counts_by_section_and_version)

# group by "Did_Exam_Prep Assignment" count of students and mean studen score
df2 = exams.groupby(by=['Did_Exam_Prep Assignment'])\
    .agg({ 'Exam_Version': 'count', 'Student_Score': 'mean' })
df2 = df2.rename(columns={'Exam_Version': 'Count_of_Students', 
                          'Student_Score': 'Mean_Student_Score'})
st.dataframe(df2)

st.header("Pivot and Melt Example")

# Get average scores by section and exam version:
avg_scores_by_section_and_version = \
    exams.groupby(by=['Class_Section', 'Exam_Version']).agg({'Student_Score': 'mean'})

# add section and exam version back to dataframe
avg_scores_by_section_and_version['Class_Section'] =\
    avg_scores_by_section_and_version.index.get_level_values('Class_Section')
avg_scores_by_section_and_version['Exam_Version'] =\
    avg_scores_by_section_and_version.index.get_level_values('Exam_Version')
# reset the index
avg_scores_by_section_and_version = avg_scores_by_section_and_version.reset_index(drop=True)
#rename the Student_score to average score
avg_scores_by_section_and_version =  avg_scores_by_section_and_version.rename(columns={'Student_Score': 'Average_Score'})
#reorder the columns
avg_scores_by_section_and_version = avg_scores_by_section_and_version[['Class_Section', 'Exam_Version', 'Average_Score']]

#show
st.dataframe(avg_scores_by_section_and_version)

# pivot
pivot1 = avg_scores_by_section_and_version.pivot(
    index='Class_Section', columns='Exam_Version', values='Average_Score')

st.dataframe(pivot1)

melted1 = pivot1.reset_index().melt(
    id_vars='Class_Section', value_name='Average_Score', var_name='Exam_Version')

st.dataframe(melted1)

st.title("Pivot Table Example")
# pivot table exams in row Class_Secton, in Columns Exam_Version, values Student_Score, aggfunc mean
pivot_table1 = exams.pivot_table(
    index='Class_Section', columns='Exam_Version', values='Student_Score', aggfunc='mean')

st.dataframe(pivot_table1)