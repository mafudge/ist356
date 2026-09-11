import streamlit as st

st.title("Area and Perimeter Calculator")

length = st.number_input("Enter the length of the rectangle:", min_value=0.0, step=0.1)
width = st.number_input("Enter the width of the rectangle:", min_value=0.0, step=0.1)

calculate_button = st.button("Calculate")
clear_button = st.button("Clear")

if calculate_button:
    area = length * width
    perimeter = 2 * (length + width)
    
    st.write(f"Area of the rectangle: {area}")
    st.write(f"Perimeter of the rectangle: {perimeter}")

if clear_button:
    length = 0.0
    width = 0.0