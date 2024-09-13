import streamlit as st

st.title('Area and permieter')
length = st.number_input("Enter Length:")
width = st.number_input("Enter Width:")
btn_clicked = st.button('Calculate!')

if btn_clicked:
    area = length * width
    perm = 2 * (length + width)
    st.write(f"Area: {area}")
    st.write(f"Perimeter: {perm}")
