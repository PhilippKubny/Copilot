import os
from dotenv import load_dotenv
import openai

from langchain_community.llms import AzureOpenAI
from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class CopilotV6:
    def __init__(self):
        # Load environment variables
        if load_dotenv():
            self.azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
            self.azure_deployment = os.getenv("AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME")
            if not self.azure_openai_endpoint:
                raise ValueError("Azure OpenAI Endpoint not found in environment variables.")
            if not self.azure_deployment:
                raise ValueError("Azure OpenAI Completion Deployment Name not found in environment variables.")
        else:
            raise FileNotFoundError("No .env file found.")

        # Initialize Azure OpenAI
        self.llm = AzureChatOpenAI(azure_deployment=self.azure_deployment)
        
        # Create a prompt template with variables, note the curly braces
        self.prompt = PromptTemplate(
            input_variables=["input"],
            template="{input}",
        )
        
        # Create a chain
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def get_answer(self, question):
        response = self.chain.invoke({"input": question})
        return response['text']