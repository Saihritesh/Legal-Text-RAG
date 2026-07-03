# Infraon Intelligent Assistant

A locally hosted, agentic support assistant for network device management.

This project combines a lightweight intent classifier (SetFit + MiniLM), LangGraph orchestration, Retrieval-Augmented Generation (RAG), and a locally hosted LLM (Qwen3 via Ollama) to provide intelligent support for network operations.

---

# Phase 0 - Foundation

## Objective

The purpose of Phase 0 is to establish the project's baseline infrastructure before implementing any AI workflows.

At the end of this phase the application should be able to:

- Run a FastAPI backend
- Communicate with a locally hosted Qwen3 model through Ollama
- Expose a REST API endpoint
- Maintain a modular project structure for future development

No classifier, LangGraph workflow, database, or vector search is implemented in this phase.

---

# Architecture

```
User
 │
 ▼
FastAPI
 │
 ▼
LLM Service
 │
 ▼
ChatOllama
 │
 ▼
Ollama
 │
 ▼
Qwen3
```

The purpose of this phase is only to verify communication between the backend and the local LLM.

---

# Project Structure

```
chatbot/

│
├── api/
│   ├── __init__.py
│   └── main.py

│
├── services/
│   ├── __init__.py
│   └── llm_service.py

│
├── config/
│   ├── __init__.py
│   └── config.py

│
├── classifier/

├── orchestration/

├── ingestion/

├── paths/

├── storage/

├── tests/

├── requirements.txt

├── .gitignore

└── README.md
```

Only the API, configuration, and LLM service are functional during Phase 0.

The remaining folders are placeholders for later phases.

---

# Components

## FastAPI

Acts as the application's backend.

Responsibilities:

- Receive user requests
- Validate request data
- Call the appropriate service
- Return responses

FastAPI contains no AI logic.

---

## LLM Service

Acts as a wrapper around LangChain.

Instead of importing ChatOllama throughout the project, every component communicates through one interface.

```
Application

↓

LLM Service

↓

ChatOllama

↓

Ollama

↓

Qwen3
```

Advantages:

- Centralized model configuration
- Easy model replacement
- Cleaner code
- Better testing

---

## Ollama

Ollama hosts the language model locally.

Responsibilities:

- Load Qwen3
- Run inference
- Expose a local HTTP API

No data leaves the local machine.

---

## Qwen3

Qwen3 is the reasoning model used throughout the application.

During Phase 0 it simply receives prompts and returns generated responses.

Later phases will use it for:

- Documentation QA
- SQL generation
- Troubleshooting
- Response summarization

---

## Configuration

All configurable parameters will be centralized.

Examples:

- model name
- temperature
- Ollama URL
- timeout values

Future phases will extend this configuration file.

---

# Installation

Create a virtual environment

```bash
python3 -m venv ollama-venv
```

Activate

```bash
source ollama-venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running Ollama

Ensure Ollama is installed.

Download the model

```bash
ollama pull qwen3:0.6b
```

Verify

```bash
ollama list
```

---

# Running FastAPI

```bash
uvicorn api.main:app --reload
```

Swagger UI

```
http://localhost:8000/docs
```

---

# Current Endpoint

POST

```
/chat
```

Example request

```json
{
    "message":"Hello"
}
```

Example response

```json
{
    "response":"Hello! How can I help you today?"
}
```

---

# Future Phases

## Phase 1

Intent Classification

- SetFit
- MiniLM
- Synthetic training dataset
- Intent prediction

---

## Phase 2

LangGraph Routing

- State machine
- Intent routing
- Memory loading

---

## Phase 3

App Information

- Qdrant
- Documentation RAG
- Grounded answers

---

## Phase 4

General Assistant

- General conversations
- Domain verification
- Session context

---

## Phase 5

Navigation

- Route embeddings
- Semantic search
- Navigation suggestions

---

## Phase 6

Database Search

- Schema RAG
- SQL generation
- SQL validation
- Read-only PostgreSQL

---

## Phase 7

Troubleshooting

- Tool registry
- Ping
- SNMP
- Log collection
- LLM diagnosis
- Retry loop

---

## Phase 8

Production Features

- Session memory
- Long-term memory
- Authentication
- Streaming responses
- Monitoring
- Logging

---

# Technologies

- FastAPI
- LangChain
- LangGraph
- Ollama
- Qwen3
- SetFit
- Sentence Transformers
- PostgreSQL
- Qdrant
- React

---

# Current Status

Phase 0 Complete

✔ Project structure

✔ FastAPI

✔ Local LLM

✔ Ollama integration

⬜ Intent Classification

⬜ LangGraph

⬜ RAG

⬜ PostgreSQL

⬜ Qdrant

⬜ Production Deployment