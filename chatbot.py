import streamlit as st
from openai import OpenAI

# Get secret from Streamlit secrets.toml
api_key = st.secrets["OPENAI_API_KEY"]
if not api_key:
    st.error("OPENAI_API_KEY is not set in .streamlit/secrets.toml.")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("OpenAI Chatbot")
grade_level=st.selectbox("Select Grade Level", 
    ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Your message here..."
"")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=st.session_state.messages
        )
        bot_reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.chat_message("assistant").write(bot_reply)