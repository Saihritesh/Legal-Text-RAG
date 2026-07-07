from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

result = embeddings.embed_query("Hello World")

print(len(result))
print(result[:5])