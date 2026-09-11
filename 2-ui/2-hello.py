import streamlit as st

st.title("Saying Hello!!")
name = st.text_input("And you are?")
age = st.slider("How old are you?",min_value=18, max_value=35, value=(35+18)//2, step=1)

mybutton = st.button("GO FOR IT", type="primary")

if mybutton:
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old.")