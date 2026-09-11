import streamlit as st

st.title("Area / Perimeter Calculator")

length = st.number_input("Length", min_value=0.0, step=0.1) 
width = st.number_input("Width", min_value=0.0, step=0.1)

#put the buttons in a horizontal layout
col1, col2,col3 = st.columns([0.25, 0.25, 0.8])
with col1:
    clear = st.button("Clear 🧹")
with col2:
    calculate = st.button("Calculate 🧮")

if clear:
    # set the ui widget values back to 0.0
    length = 0.0
    width = 0.0

if calculate:
    area = length * width
    perimeter = 2 * (length + width)
    st.success(f"Area: {area}, Perimeter: {perimeter}")