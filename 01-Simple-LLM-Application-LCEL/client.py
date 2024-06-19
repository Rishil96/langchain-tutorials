from langserve import RemoteRunnable

# Creating a remote client to hit the Langchain endpoint with inputs
remote_chain = RemoteRunnable("http://localhost:8000/chain/")
print(remote_chain.invoke({"language": "Spanish", "text": "Hi!"}))
