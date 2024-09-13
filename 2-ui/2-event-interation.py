import streamlit as st


def hi_click():
    if name:
        st.success(f"Hello, {name}", icon="👍")
    else:
        st.error(f"I can't say hello, if you don't tell me your name!", icon="💣")


def clear_click():
    name = None 

# setup
st.title("Streamlit Interaction: event-driven")
name = st.text_input("Who are you?")
st.button('Say Hi!', on_click=hi_click)
st.button('Clear', on_click=clear_click)