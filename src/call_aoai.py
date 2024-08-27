from openai import AzureOpenAI
from typing import List
from dotenv import load_dotenv, find_dotenv
from textwrap import dedent
import openai
import os
import ast
import logging

load_dotenv(find_dotenv())
print(os.getenv("AZURE_OPENAI_BASE"))
logger = logging.getLogger(__name__)
openai.log='warning'


def call_aoai(sys:str, prompt:str) -> List:

    aoai_client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_BASE"), 
        api_key=os.getenv("AZURE_OPENAI_KEY"),
        api_version="2024-02-01"
    )
    
    response = aoai_client.chat.completions.create(
        model=os.getenv("AZURE_DEPLOYMENT_NAME"), # model = "deployment_name".
        messages=[
            {"role": "system", "content": dedent(sys)},
            {"role": "user", "content": dedent(prompt)}
        ],
    )

    try:
        output = ast.literal_eval(response.choices[0].message.content)
        return output
    except Exception as e:
        logger.warning(f"{e}")
        return []

if __name__ == "__main__":
    print(call_aoai("","Output a list of length 5 with random intergers. Output ONLY the list. Example: [1,5,76,7,90]"))