# MLOps Demo Project (Bilingual: Português/English)

---

## 📑 Table of Contents

- [Português](#português)
- [English](#english)

---

<a name="português"></a>
# 🇧🇷 Português

## Objetivo do Projeto

Este projeto visa facilitar a vida de usuários que desejam obter informações por chat com base em documentos PDFs que possuam.

```
fastapi, chromadb, langchain, streamlit, httpx, slate3k, docker
```

O objetivo é criar um pipeline simples de RAG (Retrieval Augmented Generation) com LLM, demonstrando conceitos como banco vetorial, API, frontend interativo e automação.

---

## Estrutura do Projeto

```
lang_mlops/
├── backend/        # FastAPI, lógica do LLM, ChromaDB, Langchain
├── frontend/       # Streamlit app para interação do usuário
├── common/         # Utilidades e código compartilhado
├── schemas/        # Schemas Pydantic para API
├── scripts/        # Scripts auxiliares
├── pdfreader.py    # Leitura de PDFs
├── docker-compose.yaml
└── README.md
```

- **backend/**: Endpoints FastAPI, integração com LLM (via Langchain) e banco vetorial (ChromaDB).
- **frontend/**: Aplicação Streamlit para upload de PDFs, busca e interação com a LLM.

---

## Como Rodar o Projeto

### Pré-requisitos
- Python >= 3.10
- Docker & Docker Compose
- Arquivo `.env` na raiz do projeto com as variáveis necessárias

### Rodando o Projeto

Com o `.env` pronto, execute:

```sh
docker compose up -d
```

### Como Usar

- **Frontend (Streamlit):**
    - [http://localhost:8501](http://localhost:8501)
    - Faça upload de PDFs para adicionar contexto e faça perguntas baseadas neles.

- **Backend (FastAPI):**
    - Principais endpoints:
        - `/context/post` (POST): Adiciona contexto ao banco vetorial.
        - `/context/get` (GET): Busca contexto similar.
        - `/context/get/all` (GET): Retorna todo o contexto armazenado.
        - `/background` (POST): Define contexto de fundo para a LLM.
        - `/llm/response` (GET): Retorna resposta da LLM baseada no contexto.

---

## Funcionalidades

- [x] Upload de PDFs e extração de contexto (Streamlit)
- [x] Banco vetorial com ChromaDB
- [x] API com FastAPI para armazenamento e busca de contexto
- [x] Integração com LLM via Langchain
- [x] Dockerização completa

---

## Fundamentação Teórica

- **Vector DB (ChromaDB):** Utiliza embeddings para armazenar e buscar contexto textual.
- **RAG (Retrieval Augmented Generation):** Técnica para guiar respostas de LLMs com base em contexto externo.
- **Langchain:** Abstração para integração com LLMs e fluxos de RAG.

---

## O que foi aprendido

O projeto consolidou conhecimentos em orientação a objetos, RAG, embeddings, APIs, automação, integração de serviços e dockerização.


---

<a name="english"></a>
# 🇬🇧 English

## Project Purpose

This project is intended for users who want to get information from their own PDF documents through a chat-like experience.

```
fastapi, chromadb, langchain, streamlit, httpx, slate3k, docker
```

The goal is to create a simple RAG pipeline with LLM, demonstrating concepts such as vector database, API, interactive frontend, and automation.

---

## Project Structure

```
lang_mlops/
├── backend/        # FastAPI, LLM logic, ChromaDB, Langchain
├── frontend/       # Streamlit app for user interaction
├── common/         # Utilities and shared code
├── schemas/        # Pydantic schemas for API
├── scripts/        # Auxiliary scripts
├── pdfreader.py    # PDF reading
├── docker-compose.yaml
└── README.md
```

- **backend/**: FastAPI endpoints, integration with LLM (via Langchain) and vector DB (ChromaDB).
- **frontend/**: Streamlit app for PDF upload, search, and LLM interaction.

---

## How to Run

### Prerequisites
- Python >= 3.10
- Docker & Docker Compose
- `.env` file at the project root with the required variables

### Running the Project

```

### Rodando o Projeto | Running the Project

Com o `.env` pronto, execute:
With the `.env` file ready, run:

```sh
docker compose up -d
```

### Como Usar | How to Use

- **Frontend (Streamlit):**
    - [http://localhost:8501](http://localhost:8501)
    - Faça upload de PDFs para adicionar contexto e faça perguntas baseadas neles.
    - Upload PDFs to add context and ask questions based on them.

- **Backend (FastAPI):**
    - Endpoints principais:
        - `/context/post` (POST): Adiciona contexto ao banco vetorial.
        - `/context/get` (GET): Busca contexto similar.
        - `/context/get/all` (GET): Retorna todo o contexto armazenado.
        - `/background` (POST): Define contexto de fundo para a LLM.
        - `/llm/response` (GET): Retorna resposta da LLM baseada no contexto.
    - Main endpoints:
        - `/context/post` (POST): Add context to the vector database.
        - `/context/get` (GET): Search for similar context.
        - `/context/get/all` (GET): Get all stored context.
        - `/background` (POST): Set background context for the LLM.
        - `/llm/response` (GET): Get LLM response based on context.

---

## Funcionalidades | Features

- [x] Upload de PDFs e extração de contexto (Streamlit)
- [x] Banco vetorial com ChromaDB
- [x] API com FastAPI para armazenamento e busca de contexto
- [x] Integração com LLM via Langchain
- [x] Dockerização completa
- [ ] Orquestração automática com Airflow (em desenvolvimento)

---

## Fundamentação Teórica | Theoretical Foundation

- **Vector DB (ChromaDB):**
    - Utiliza embeddings para armazenar e buscar contexto textual.
    - Uses embeddings to store and search textual context.

- **RAG (Retrieval Augmented Generation):**
    - Técnica para guiar respostas de LLMs com base em contexto externo.
    - Technique to guide LLM responses based on external context.

- **Langchain:**
    - Abstração para integração com LLMs e fluxos de RAG.
    - Abstraction for integrating with LLMs and RAG pipelines.

---

## O que foi aprendido | What I Learned

O projeto consolidou conhecimentos em orientação a objetos, RAG, embeddings, APIs, automação, integração de serviços e dockerização.
The project consolidated knowledge in OOP, RAG, embeddings, APIs, automation, service integration, and dockerization.



- Aqui voce vera os esqueletos de cada endpoint do fastapi que o modelo esta utilizando para a llm 
[Endpoints da llm fastapi](http://localhost:8000)