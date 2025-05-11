import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into environment

def get_api_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise ValueError("❌ Please set OPENAI_API_KEY in .env file.")
    return key
