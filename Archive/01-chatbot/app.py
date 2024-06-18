from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template to initially set up the model to be a chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question:{question}")
    ]
)

# Create streamlit frontend
st.title("Langchain demo with OpenAI API")
input_text = st.text_input("Search the topic you want")

# Use OpenAI LLM model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create an output parser
output_parser = StrOutputParser()

# Create a chain of all created components
chain = prompt | llm | output_parser

# When we give input in frontend, and press enter, we should get the output
if input_text:
    st.write(chain.invoke({"question": input_text}))
