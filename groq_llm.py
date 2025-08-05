from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
def get_llm():
    """Initialize Groq LLM."""
    return ChatGroq(
        model_name="llama3-70b-8192",  # You can also use llama2 or gemma models
        temperature=0.2,
        groq_api_key=groq_api_key  # Replace with your Groq API key
    )
