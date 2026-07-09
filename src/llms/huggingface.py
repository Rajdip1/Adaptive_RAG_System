"""
Hugging Face LLM initialization and configuration.
"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Set API token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv(
    "HUGGINGFACEHUB_API_TOKEN", ""
)

# Create Hugging Face endpoint
hf_llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512,
)

# Chat wrapper
llm = ChatHuggingFace(llm=hf_llm)