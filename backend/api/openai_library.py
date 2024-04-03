import openai
import os
import dotenv
from openai import AzureOpenAI

if dotenv.load_dotenv():
    print(f'Found .env file in storage')
else:
    print('No configurated .env file available')

# Initializing the client
client = AzureOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    api_key=os.getenv('AZURE_OPENAI_API_KEY'),
    api_version=os.getenv('OPENAI_API_VERSION')
)

response = client.chat.completions.create(
    model=os.getenv('AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME'),
    messages=[{'role': 'assistant', 'content': 'You are a helpful copilot for students'}]
)

print(response.choices[0].message.content)