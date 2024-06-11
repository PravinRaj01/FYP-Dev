import streamlit as st
import logging
from PIL import Image, ImageEnhance
import base64

logging.basicConfig(level=logging.INFO)

# Function to convert image to base64
def img_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Streamlit Page Configuration
st.set_page_config(
    page_title="Malaysian Code-Switched Language Translator",
    page_icon=":earth_asia:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("About")
markdown = """
This is a machine translation system developed to translate Malaysian code-switched language using Large Language Model (LLM).

&nbsp;
&nbsp;

This translator can translate "Malay - English" code-switched language to "English".

&nbsp;
&nbsp;

Developed by:
**PRAVIN RAJ A/L MURALITHARAN**
"""
st.sidebar.info(markdown)

# Dark Mode / Light Mode Toggle
is_dark_mode = st.sidebar.checkbox("Dark Mode", value=True)

# Basic Instructions
st.sidebar.title("Basic Instructions")
st.sidebar.markdown("""
- **Enter Code-Switched Text**: Type your Malay-English code-switched text in the prompt box.
- **Convert**: Click the 'Convert' button to translate the text to English.
- **View Results**: The translated text will be displayed below the prompt box.
""")

# Custom CSS based on mode
if is_dark_mode:
    st.markdown("""
        <style>
        body {
            background-color: #222629;
            color: #F2F2F2;
        }
        .sidebar .sidebar-content {
            background-color: #222629;
        }
        .sidebar .sidebar-content h2, .sidebar .sidebar-content h3, .sidebar .sidebar-content h4, .sidebar .sidebar-content p {
            color: #F2F2F2;
        }
        .stTextInput > div > div > input {
            background-color: #5A7D7B;
            color: #F2F2F2;
        }
        .stButton > button {
            background-color: #65CCB8;
            color: white;
        }
        .st-chat-input {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #222629;
            color: #F2F2F2;
            padding: 10px;
        }
        .st-chat-input input {
            width: 85%;
            background-color: #5A7D7B;
            color: #F2F2F2;
            border: none;
            padding: 10px;
        }
        .st-chat-input button {
            width: 10%;
            background-color: #65CCB8;
            color: white;
            border: none;
            padding: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body {
            background-color: #D6DADD;
            color: #1A1A1A;
        }
        .sidebar .sidebar-content {
            background-color: #D6DADD;
        }
        .sidebar .sidebar-content h2, .sidebar .sidebar-content h3, .sidebar .sidebar-content h4, .sidebar .sidebar-content p {
            color: #1A1A1A;
        }
        .stTextInput > div > div > input {
            background-color: #5A7D7B;
            color: #1A1A1A;
        }
        .stButton > button {
            background-color: #78D2C0;
            color: white;
        }
        .st-chat-input {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #D6DADD;
            color: #1A1A1A;
            padding: 10px;
        }
        .st-chat-input input {
            width: 85%;
            background-color: #5A7D7B;
            color: #1A1A1A;
            border: none;
            padding: 10px;
        }
        .st-chat-input button {
            width: 10%;
            background-color: #78D2C0;
            color: white;
            border: none;
            padding: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

# Main content
st.title("Malaysian Code-Switched Language Translator")
st.markdown("<h3 style='text-align: center;'>ENTER YOUR CODE-SWITCHED TEXT IN THE PROMPT BOX BELOW</h3>", unsafe_allow_html=True)

# Placeholder for the translation result
if "translation_result" in st.session_state:
    st.write("Translated Text:")
    st.write(st.session_state.translation_result)

# Chat input styled at the bottom
st.markdown("""
    <div class="st-chat-input">
        <form action="#" method="post">
            <input type="text" name="chat_input" id="chat_input" placeholder="Enter your code-switched text here...">
            <button type="submit">Send</button>
        </form>
    </div>
    """, unsafe_allow_html=True)

# Process the input from the form
query_params = st.experimental_get_query_params()
chat_input = query_params.get("chat_input", [""])[0]
if chat_input:
    # Placeholder for the translation logic
    translation_result = chat_input  # Replace with actual translation function call
    st.session_state.translation_result = translation_result
    st.experimental_set_query_params()  # Clear the input field
    st.experimental_rerun()  # Refresh the page to display the result
