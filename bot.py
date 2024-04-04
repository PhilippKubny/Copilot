import streamlit as st
from langchain_openai import AzureChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

def get_response_from_input(user_input) -> str:
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv('AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME'),
        api_key=os.getenv('AZURE_OPENAI_API_KEY')
    )

    template = 'You are a helful copilot for a student. Can you anwer the following question: {input}'
    
    promt_template = PromptTemplate(
        input_variables=['input'],
        template=template
    )

    chain = LLMChain(llm=llm, prompt=promt_template)

    response = chain.invoke({'input': f'{user_input}'})

    return response['text']


if load_dotenv():
    print("Found Azure OpenAI Endpoint: " + os.getenv("AZURE_OPENAI_ENDPOINT"))
else: 
    print("No file .env found")

st.title("Manu's copilot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
prompt = st.chat_input('Your Question')

if prompt:
    # Display user message in chat message container
    # Markdown is used to format the output
    st.chat_message('user').markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response_from_input(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

