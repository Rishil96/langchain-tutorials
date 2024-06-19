# Library imports
import uvicorn
from typing import List
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from langserve import add_routes


# Step 1: Creating the prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}")
    ]
)

# Step 2: Create the LLM Instance
model = Ollama(model="llama2")

# Step 3: Create the output parser
parser = StrOutputParser()

# Step 4: Create the chain of components
chain = prompt_template | model | parser

# Step 5: FastAPI definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces"
)

# Step 6: Add the chain route
add_routes(
    app,
    chain,
    path="/chain"
)

# Start serving 
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

# To test the API via browser, go to localhost/{path}/playground
# We would have an interface to try out our model