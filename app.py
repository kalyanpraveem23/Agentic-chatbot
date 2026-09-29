from agentic_chatbot_backend import chatbot
from langchain_core.messages import HumanMessage
import streamlit as st

st.title("Agentic Chatbot with LangGraph")

CONFIG = {
    "configurable": {
        "thread_id": "thread-1"
    }
}

# Initialize chat history
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# Display previous messages
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type here")

if user_input:

    # Display user message
    st.session_state["message_history"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Get chatbot response
    with st.chat_message("assistant"):

        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {
                    "messages": [
                        HumanMessage(content=user_input)
                    ]
                },
                config=CONFIG,
                stream_mode="messages"
            )
        )

    # Save assistant response
    st.session_state["message_history"].append({
        "role": "assistant",
        "content": ai_message
    })