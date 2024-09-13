import streamlit as st

# Streamlit is always running, so only do this will not do what you think

count = 0

# widget setup
st.title('Counter Example: Wrong')
st.write("variables that change based on previous runs will not work as expected ")
st.write("this is because streamlit runs all this code with each interaction")
incr_clicked = st.button('increment counter', type='primary')
reset_clicked = st.button('reset counter', type='secondary')

# interactions
if reset_clicked:
    count = 0
elif incr_clicked:
    count = count + 1
    
# display session state, after interations
st.write(f'Button clicked {count} times')
