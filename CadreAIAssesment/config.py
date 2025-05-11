import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the system environment
load_dotenv()  # loads variables from .env into environment

# Function to retrieve the OpenAI API key from environment variables
def get_api_key():
    key = os.getenv("OPENAI_API_KEY")  # Fetch the API key from the environment
    if not key:
        # Raise an error if the key is not found
        raise ValueError("❌ Please set OPENAI_API_KEY in .env file.")
    return key  # Return the API key for use
