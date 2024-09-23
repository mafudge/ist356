import streamlit as st
import pandas as pd

def grade(participation: float) -> str:
    if participation == 0.0:
        return "AB"
    
    if participation <= 0.5:
        return "np"
    
    return "+"

dates = ['2024-01-08', '2024-01-15', '2024-01-22', '2024-01-29']
base = "https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/student_polls"

st.title("Xavier Polling Processor")

# load in the roster
roster_df = pd.read_csv(f'{base}/roster.csv')

# load in the polls
polls = []
for date in dates:
    poll = pd.read_csv(f'{base}/poll-responses-{date}.csv')
    poll['date'] = date
    poll['poll_count'] = poll['poll_num'].max()
    polls.append(poll)
polls_df = pd.concat(polls, ignore_index=True)

# join the roster to the polls, left join for absent students.
combined_df = pd.merge(roster_df, polls_df, how='left', left_on='netid', right_on='student_id')
st.dataframe(combined_df)

# poll counts by date
poll_counts = combined_df.pivot_table(index='date', values='poll_num', aggfunc='max')
st.write("Poll Counts")
st.dataframe(poll_counts)

# student reponses by date
student_responses = combined_df.pivot_table(index='netid', columns='date', values='answer', aggfunc='count')
student_responses = student_responses.fillna(0)
st.write("Student Responses")
st.dataframe(student_responses)

# responses as percentages
student_pct = student_responses.copy()
for col in student_pct.columns:
    student_pct[col] = student_responses[col] / poll_counts.loc[col, 'poll_num']
st.write("Student Percentages")
st.dataframe(student_pct)


# graded responses
student_graded = student_pct.copy()
for col in student_graded.columns:
    student_graded[col] = student_graded[col].apply(grade)
st.write("Student Gradeed")
st.dataframe(student_graded)


# summary dataframe
summary = student_graded.copy()
summary['sessions'] = summary.count(axis=1)
summary['AB'] = summary.apply(lambda row: row.value_counts().get('AB', 0), axis=1)
summary['np'] = summary.apply(lambda row: row.value_counts().get('np', 0), axis=1)
summary['pct_AB_or_np'] = (summary['AB']  + summary['np'])/ summary['sessions']
summary['netid'] = summary.index
summary = summary.reset_index(drop=True)
summary = pd.merge(summary, roster_df, how='inner', left_on='netid', right_on='netid')
summary = summary[['netid','name','sessions', 'AB', 'np', 'pct_AB_or_np']]
st.write("Summary")
st.dataframe(summary)
st.download_button("Download Summary", summary.to_csv(header=True), "summary.csv", "text/csv")