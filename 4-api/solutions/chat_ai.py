import os
import streamlit as st
import requests
import dotenv

dotenv.load_dotenv()

CENT_API_KEY = os.getenv("CENT_API_KEY")

prompts = [
    "You are a playful teenager named Alex. You really like emoji.",
    "You are an AI assistant that talks like a pirate. Who always brings the conversation back to the sea.",
    "You are an AI assistant that thinks you are a Shakespearean actor.",
    "You are a fact-answering robot. Straightforward and literal. You add beeps and clicks to your speech.",
    "You are wise cracking, joke telling AI assistant. You are witty, sarcastic and full of one-liners.",
]

def generate_ai_response(context):
    url = "https://portal.app.cent-su.org/api/ollama/chat/completions"
    params = { "model": "llama3.2:latest", "stream": False, "temperature": 0.7, "max_tokens": 12000 }
    response = requests.post(url, json=context, headers={"X-API-KEY": CENT_API_KEY}, params=params)
    response.raise_for_status()
    results = response.json()
    content =  results["choices"][0]["message"]["content"]
    return content

st.title("Chat AI.")
st.caption("Let's help you understand system prompts and context.")
prompt_column, clear_column = st.columns([4, 1], vertical_alignment="bottom")
system_prompt = prompt_column.selectbox("Select a system prompt", prompts)
if clear_column.button("Clear", use_container_width=True):
    st.session_state.messages = []

if system_prompt:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # don't clear history on subsequent runs, just update the system prompt
    if st.session_state.messages and st.session_state.messages[0]["role"] == "system":
        st.session_state.messages[0]["content"] = system_prompt
    else:
        st.session_state.messages.insert(0, {"role": "system", "content": system_prompt})

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    prompt = st.chat_input("?")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Generating response..."):

            response = generate_ai_response(st.session_state.messages)
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})