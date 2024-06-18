from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


# Prompt template: which tells the model what we are expecting from it. Basically an initial setup for the model.
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant named Rishil. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Streamlit framework: helps creating a basic frontend to interact with our LLM
st.title("Langchain demo with LLAMA2 API")
input_text = st.text_input("Search the topic you want")

# ollama model
llm = Ollama(model="llama2")                # Connect to llama2 model
output_parser = StrOutputParser()           # Decide how the model output should be parsed
chain = prompt | llm | output_parser        # Create a chain to combine multiple components to a single process

if input_text:
    st.write(chain.invoke({"question": input_text}))
