import streamlit as st

# Streamlit is always running, so only do this when count is not in session_state

# initialize
if 'count' not in st.session_state:
    st.session_state.count = 0

# widget setup
st.title('Counter Example: Session State')
st.write("variables that change based on previous runs need session state")
st.write("`st.session_state` preserves the values of the variable between runs")
incr_clicked = st.button('increment counter', type='primary')
reset_clicked = st.button('reset counter', type='secondary')

# interactions
if reset_clicked:
    st.session_state.count = 0
elif incr_clicked:
    st.session_state.count = st.session_state.count + 1
    
# display session state, after interations
st.write(f'Button clicked {st.session_state.count} times')
