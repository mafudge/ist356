import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count = 0

def incr_button_clicked():
    st.session_state.count = st.session_state.count + 1

def reset_button_clicked():
    st.session_state.count = 0

st.title('My first app')
st.write('Welcome to my first app on Streamlit!')
st.selectbox('Select a number', [1,2,3,4,5])

cols = st.columns([1,1,3])
with cols[0]:
    st.button('increment', on_click=incr_button_clicked, key='incr_button', type='primary')
with cols[1]:
    st.button('reset', on_click=reset_button_clicked, key='reset_button', type='secondary')

st.write(f'Button clicked {st.session_state.count} times', key='output')




