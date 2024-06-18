from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# Initialize all environment variables
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="LangChain Server", version="1.0", description="A simple API Server")

# Add a route in our fastapi app using function add routes from langserve
add_routes(app, ChatOpenAI(), path="/openai")

# Create both OpenAI and LLAMA2 model instances
model = ChatOpenAI()
llm = Ollama(model="llama2")

# Create prompts to tell the LLM what are we expecting from it
prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} with 50 words")
prompt2 = ChatPromptTemplate.from_template("Write an poem about {topic} with 50 words")

# Add route to use OpenAI LLM to write an essay
add_routes(app, prompt1 | model, path="/essay")

# Add route to use LLAMA2 model to write a poem
add_routes(app, prompt2 | llm, path="/poem")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
