# app/helpers/streamlit_helpers.py

import json
import uuid
import os

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain import hub

try:
    from common.prompts import WELCOME_MESSAGE
except Exception as e:
    from ..common.prompts import WELCOME_MESSAGE
    

def get_logger(name):
    """
    Retrieve a Streamlit logger instance.

    :param name: The name for the logger
    :return: Logger instance
    """
    from streamlit.logger import get_logger
    return get_logger(name)

logger = get_logger(__name__)

def configure_page(title, icon):
    """
    Configure the Streamlit page settings: page title, icon, and layout.
    Also applies minimal styling for spacing.

    :param title: The title of the page
    :param icon: The favicon/icon for the page
    """
    st.set_page_config(page_title=title, page_icon=icon, layout="wide")
    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 2rem;
                padding-bottom: 0rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def get_or_create_ids():
    """
    Generate or retrieve session and user IDs from Streamlit's session_state.

    :return: (session_id, user_id)
    """
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())
        logger.info("Created new session_id: %s", st.session_state["session_id"])
    else:
        logger.info("Found existing session_id: %s", st.session_state["session_id"])

    if "user_id" not in st.session_state:
        st.session_state["user_id"] = str(uuid.uuid4())
        logger.info("Created new user_id: %s", st.session_state["user_id"])
    else:
        logger.info("Found existing user_id: %s", st.session_state["user_id"])

    return st.session_state["session_id"], st.session_state["user_id"]

def initialize_chat_history(model):
    """
    Initialize the chat history with a welcome message from the AI model.
    By default, attempts to pull a prompt from the prompts library if WELCOME_PROMPT_NAME is set,
    otherwise uses a fallback string.

    :param model: The name of the model (for logging or referencing)
    """
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [AIMessage(content=WELCOME_MESSAGE)]
        logger.info("Chat history initialized for model: %s", model)
    else:
        logger.info("Chat history already exists for model: %s", model)

def display_chat_history():
    """
    Render the existing chat history in Streamlit:
    - AI messages labeled "AI"
    - Human messages labeled "Human"
    """
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
            logger.info("Displayed AI message: %s", message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)
            logger.info("Displayed Human message: %s", message.content)

def autoplay_audio(file_path):
    """
    Play an audio file in the user's browser automatically using an <audio> tag.

    :param file_path: The path to the WAV file to play
    """
    import base64
    if not os.path.exists(file_path):
        logger.error("Audio file does not exist: %s", file_path)
        return

    with open(file_path, "rb") as audio_file:
        audio_data = audio_file.read()

    audio_base64 = base64.b64encode(audio_data).decode("utf-8")
    audio_html = f"""
    <audio autoplay>
        <source src="data:audio/wav;base64,{audio_base64}" type="audio/wav">
    </audio>
    """
    st.markdown(audio_html, unsafe_allow_html=True)
    logger.info("Autoplayed audio: %s", file_path)
