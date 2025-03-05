# O que é esse projeto?

Esse é um projeto que visa demonstrar algumas habilidades de MLOps com as seguinte stacks:

fastapi, chromadb, langchain, streamlit, httpx e docker

O projeto é um RAG simples utilizando o modelo local do Ollama com a intenção direta de mostrar minhas habilidades

# Como rodar o projeto

Primeiramente é necessário ter o docker compose instalado e rodar o seguinte comando na raiz do projeto

```
docker compose up -d 
```

Agora que o projeto está funcionando basta colocar o seguinte link no browser

[localhost:8501](localhost:8501)

A sidebar do site serve para colocar os contextos desejados no banco de dados e na página principal <br>
para passar o prompt com RAG para o modelo