import requests
import streamlit as st


# Getting response from OpenAI model
def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={'input': {'topic': input_text}})
    return response.json()["output"]


# Getting response from LLAMA2 model
def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", json={'input': {'topic': input_text}})
    return response.json()["output"]


# Streamlit frontend logic
st.title("LangChain Demo with OpenAI and Ollama")
input_text1 = st.text_input("Write an essay on")
input_text2 = st.text_input("Write an poem on")


# Get value from input box of streamlit
if input_text1:
    st.write(get_openai_response(input_text1))

if input_text2:
    st.write(get_ollama_response(input_text2))
