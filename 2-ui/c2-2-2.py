import streamlit as st

st.title("Order Tracker")

#initialize variables
if 'total' not in st.session_state:
    st.session_state.total = 0
    st.session_state.history = []

# Inputs
amount = st.number_input("Order Amount:")
total_button = st.button("Calculate Total", 
                         type="primary")
clear_button = st.button("Clear")

# Process Avoid outputting, just manip data
if total_button:
    st.session_state.total += amount
    st.session_state.history.append(amount)

if clear_button:
    st.session_state.total = 0
    st.session_state.history = []

# outputs
st.write(f"Total Order: {st.session_state.total}")
st.write(f"History: {st.session_state.history}")