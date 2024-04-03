import json 
import os
import requests
import dotenv

if dotenv.load_dotenv():
    print(f'Found .env file in storage')
else:
    print('No configurated .env file available')

API_KEY = os.getenv('AZURE_OPENAI_API_KEY') # Receiving the API key from the .env file
API_VERSION = os.getenv('OPENAI_API_VERSION') # Receiving the API version
RESOURCE_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT') # Receiving the API Endpoint link
DEPLOYMENT_ID = os.getenv('AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME') # Receiving the deployment name of the ai model

# Constructing the url
url = f'{RESOURCE_ENDPOINT}/openai/deployments/{DEPLOYMENT_ID}/chat/completions?api-version={API_VERSION}'

print(url)

# Send request to the endpoint
r = requests.post(url, headers={'api-key': API_KEY}, json={'messages': [{'role': 'assistant', 'content': 'You are an helpful copilot for students'}]})

print(json.dumps(r.json(), indent=2))