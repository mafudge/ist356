import streamlit as st

st.title("Saying Hello.")
name = st.text_input("And you are?")

if name:
    st.write(f"Hello, {name}!")