import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# ---------------------------------------------------
# LOAD ENVIRONMENT VARIABLES
# ---------------------------------------------------

load_dotenv()

# ---------------------------------------------------
# LOAD LLM MODEL
# ---------------------------------------------------

def get_model():

    # GET API KEY FROM .env FILE
    api_key = os.getenv("GROQ_API_KEY")

    # CHECK IF API KEY EXISTS
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found in environment variables"
        )

    # INITIALIZE GROQ MODEL
    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=700
    )

    return llm