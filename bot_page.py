import streamlit as st
from st_pages import show_pages_from_config, add_page_title,show_pages, Page
from langchain_openai import AzureChatOpenAI
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from db_handler import JSONDatabase

def get_response_from_input(user_input) -> str:
    llm = AzureChatOpenAI(
        azure_deployment=os.getenv('AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME'),
        api_key=os.getenv('AZURE_OPENAI_API_KEY')
    )

    data = st.session_state.db.read_data()

    template = f"""You are a helful copilot for a student. This students primary learning preference is 
                    {data['user_data']['primary_preference']}. Make sure to take their preference into account but not only that medium.
                    Furthermore his knowledge on the learning subject is at {data['user_data']['knowledge']} level. Can you anwer the following question:""" + '{input}'
    
    promt_template = PromptTemplate(
        input_variables=['input'],
        template=template
    )

    chain = LLMChain(llm=llm, prompt=promt_template)

    response = chain.invoke({'input': f'{user_input}'})

    return response['text']


show_pages([
    Page("bot_page.py", "Copilot", "🏠"),
    Page("pages/user_profile_form_page.py", "User profile", ":books:"),
    Page("pages/calendar_page.py", "Calendar", ":calendar:")
])


if 'env_loaded' not in st.session_state:
    # Loading the environment
    if load_dotenv():
        print("Found Azure OpenAI Endpoint: " + os.getenv("AZURE_OPENAI_ENDPOINT"))
        st.session_state.env_loaded = True
    else: 
        print("No file .env found")
        st.session_state.env_loaded = False

# Initialize database
if "db" not in st.session_state:
    st.session_state.db = JSONDatabase('db.json')
if st.session_state.db.read_data():
    data = st.session_state.db.read_data()
else:
    # Setting up database
    data = {}
    data['filled_out_form'] = False
    st.session_state.db.write_data(data)


try:
    st.title(f"{data['user_data']['user_name']}'s copilot")
except:
    st.title(f"Your copilot")
st.image('qhack.png')
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

    # Check wheter the user filled out the form
    data = st.session_state.db.read_data()
    if data['filled_out_form']:
        response = get_response_from_input(prompt)
    else:
        response = "Please complete the User Profile Form"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

