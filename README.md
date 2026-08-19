# A Simple RAG Application

A small learning project built to understand the fundamentals of **Retrieval-Augmented Generation (RAG)**.

This project uses a collection of **legal text** as a knowledge base and builds a simple RAG pipeline using **ChromaDB** for vector storage and retrieval, with **Qwen3 0.6B** running locally through Ollama for generation.

The goal wasn't to build anything production-grade — it was simply to learn how the pieces of a RAG system fit together and get a working implementation up and running quickly.

## Tech Stack

- Python
- LangChain
- ChromaDB
- Ollama
- Qwen3 0.6B
- Legal text dataset

## Model

The LLM used for generation is:

    model = OllamaLLM(model="qwen3:0.6b")

The model runs locally using Ollama.

## How It Works

    Legal Text Dataset
            ↓
       Text Processing
            ↓
         Embeddings
            ↓
         ChromaDB
            ↓
        User Query
            ↓
      Similarity Search
            ↓
      Retrieved Context
            ↓
            LLM
            ↓
         Response

The basic pipeline is:

1. Load and process the legal text.
2. Generate embeddings for the documents.
3. Store the embeddings in ChromaDB.
4. Take a user query and retrieve semantically relevant documents.
5. Pass the retrieved context along with the query to the LLM.
6. Generate a response grounded in the retrieved context.

## Project Structure

    .
    ├── data/              # Legal text used as the knowledge base
    ├── main.py            # Main RAG application
    ├── vector.py          # Embedding and ChromaDB pipeline
    ├── test_embed.py      # Embedding-related testing
    └── README.md

## What I Learned

This project was a hands-on introduction to the core components of RAG:

- Document ingestion and preprocessing
- Text chunking
- Embedding generation
- Vector databases
- Similarity search
- Retrieval-Augmented Generation
- Using ChromaDB for vector retrieval
- Using LangChain to connect the components
- Running local LLMs with Ollama
- Building an end-to-end RAG pipeline

The project was built as a quick learning exercise to go from understanding the concepts behind RAG to implementing a working system.

## Limitations

This is intentionally a **simple learning project**, not a production-ready legal RAG system.

It does not include advanced retrieval techniques, reranking, sophisticated evaluation, production monitoring, or legal-domain safeguards.

The purpose was to understand the fundamentals rather than optimize every component.

## Why This Project?

The objective was simple:

> Learn RAG by building one from scratch.

Rather than jumping directly into a complicated architecture, I wanted to understand the fundamentals first — how documents become embeddings, how vector search retrieves relevant context, and how that context is ultimately passed to an LLM.

A small project, but a useful first step into building more advanced RAG and agentic AI systems.
