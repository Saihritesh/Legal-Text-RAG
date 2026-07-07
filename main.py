from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
model = OllamaLLM(model = "qwen3:0.6b")

template = """
You are an expert in answering questions about historical legal cases , 
here are some of the older cases{cases} , and here are some questions {question} about the older cases. 
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model #simple single chain
while True : 
    print("+----------------------------+")
    question = input("Ask your question :(press q to quit) ")
    print("+----------------------------+")
    if question.lower() == "q" : 
        break
    retrieved_cases = retriever.invoke(question)
    result = chain.invoke({"cases": retrieved_cases, "question": question})
    print(result)
