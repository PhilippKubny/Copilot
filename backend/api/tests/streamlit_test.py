import streamlit as st

st.title('Student Copilot')

# Promt is the user input
promt = st.chat_input('Enter your Question')

if promt:
    with st.chat_message('user'):
        st.markdown(promt)
