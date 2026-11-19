
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

st.title("AI Chatbot")

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

input_user = st.chat_input("Enter your message")

if input_user:
    chat_history.append(HumanMessage(content=input_user))

    with st.chat_message("user"):
        st.write(input_user)

    result = model.invoke(chat_history)

    chat_history.append(AIMessage(content=result.content))

    with st.chat_message("assistant"):
        st.write(result.content)
