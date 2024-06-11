import logging
import streamlit as st

# Streamlit Page Configuration
st.set_page_config(
    page_title="ROJAK | Malaysian Code-Switched Language Translator",
    page_icon="image/logo4.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://github.com/PravinRaj01/",
        "Report a bug": "https://github.com/PravinRaj01/",
        "About": """
            ## Malaysian Code-Switched Language Translator
            
            **GitHub**: https://github.com/PravinRaj01/
            
            This is a machine translation system developed to
            translate Malaysian code-switched language using Large Language Model (LLM).
            This translator can translate "Malay - English" code-switched language to "English".

            Developed by:
            **PRAVIN RAJ A/L MURALITHARAN**

        """
    }
)



# Streamlit Title
st.markdown('<h1 style="color: #65CCB8;">Malaysian Code-Switched Language Translator</h1>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 18px; color: #F2F2F2;">🤖 Enter your code-switched text in the prompt box below</p>', unsafe_allow_html=True)


# main function
def main():
    st.sidebar.image("image/logo3.png", use_column_width=True)

    
    st.sidebar.title("Basic Instructions")
    st.sidebar.markdown("""
    - **Enter Code-Switched Text**: Type your Malay-English code-switched text in the prompt box.
    - **Translate**: Click the 'Send' icon to translate the text to English.
    - **View Results**: The translated text will be displayed above the prompt box.
    """)
    st.sidebar.markdown("---")

    st.sidebar.title("Dark Mode:")
    show_advanced_info = st.sidebar.toggle("On/Off (Under Maintenance)", value=True)

    st.sidebar.markdown("---")

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



    # Handle Chat and Update Modes
    chat_input = st.chat_input("Enter your code-switched text here")
    # Placeholder for additional functionality
    # if chat_input:
    #     latest_updates = load_streamlit_updates()
    #     on_chat_submit(chat_input, api_key, latest_updates, use_langchain)

if __name__ == "__main__":
    main()
