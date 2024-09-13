import streamlit as st
import random 

def generate_ai_response(prompt):
    last_word= prompt.strip().lower().split()[-1]
    responses = [
        f"Fasinating. Tell me more about {last_word}",
        f"I find {last_word} interesting",
        f"I find {last_word} boring",
        f"Can you explain {last_word}",
        f"I'm not sure I understand {last_word}",
        f"What exactly is {last_word}",
        "You crazy."
    ]
    return random.choice(responses)

st.title("Chat Dum-E-E.")
st.caption("Generally stupid conversational AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
prompt = st.chat_input("What is up?")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


    response = generate_ai_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})