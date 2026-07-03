'''from langchain_ollama import ChatOllama

# Initialize the local model
llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0.7,
)

# Fixed prompt
prompt = """
Explain what Few Shot Learning is in simple terms.
"""

# Invoke the model
response = llm.invoke(prompt)

print(response.content)'''
for i in range(1 , 2) :
    print(i)