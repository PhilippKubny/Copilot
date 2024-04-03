from langchain_openai import AzureOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage
import os
import openai
from dotenv import load_dotenv

if load_dotenv():
    print("Found Azure OpenAI Endpoint: " + os.getenv("AZURE_OPENAI_ENDPOINT"))
else: 
    print("No file .env found")

# Create an instance of Azure OpenAI
llm = AzureChatOpenAI(
    azure_deployment = os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME")
)

# Define the prompt we want the AI to respond to - the message the Human user is asking
msg = HumanMessage(content="Explain step by step. How old is the president of USA?")

# Call the API
r = llm.invoke([msg])

# Print the response
print(r.content)