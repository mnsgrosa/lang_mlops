# Objetivo do projeto, como rodar o projeto, o que aprendi fazendo esse projeto e fundamentacao teorica

## 1. Teoria por de tras dos principais conceitos utilizados

- Embeddings
 e uma tecnica de machine learning que permite converter tipos categoricos em vetores para que facilite o treinamento de uma rede neural, irei utilizar um exemplo nao convencional e um convecional logo em seguida. O primeiro exemplo seria discretizacao de uma variavel, digamos que temos idades de pessoas de 0 a 90 anos para indicar peso, se jogado na mlp por exemplo alguem de 90 anos seria um indicador muito mais forte que alguem recem nascido para o gradiente e poderia passar a mensagem errada para o modelo entao seria melhor categorizar por faixas etarias (que nao estao separadas de maneira convencional apenas um exemplo) as idades como de 0 a 11 anos crianca(0), de 12 a 18 adolescente(1), de 19 a 30 jovem adulto(2), 31 a 70 adulo(3) e em diante idoso(4), teriamos 5 classes e teriamos um vetor possivel de ser treinado para passar a ideia ao modelo conforme os dados. O segundo exemplo e mais utilizado sao embeddings para texto, existem diversas maneiras de criar os vetores de texto darei um exemplo ilustrativo da ideia, digamos que criamos um vetor com base no contexto da palavra "correr" caso jogue ela em algum contexto como "Irei fazer uma corrida para treinar" e uma frase com giria "O corre do dia a dia e dificil" a depender de como treinamos o embedding a primeira frase seria mais proxima que a segunda frase, digamos que treinamos com o sentido de exercicio, ja que ela indica um sentido parecido com a original. O que tirar daqui e a seguinte mensagem, E muito mais facil treinar vetores para o modelo que jogar um produto de numeros e esperar que o modelo adapte-se ao produto, no exemplo de idades seria bem dificil ja que o gradiente sempre tenderia a idade maiores e para texto e necessario converter para numeros e de maneiras mais ingenuas nao daria certo. 

- Vector db(Chroma db sendo utilizado)
 ele utiliza o conceito de embeddings utilizado em series temporais e NLP para armazenar nao apenas dados textuais mas tambem imagens, no contexto do projeto e criado um vetor para os arquivos textuais em que sera utilizado para procurar por topicos parecidos, digamos que temos uma frase armazenada da seguinte maneira "CNNs sao arquiteturas de visao computacional" caso utilizemos a seguinte frase para procurar no banco de dados "Arquitetura visao computacional" teremos um vetor com certa similaridade com o contexto inserido na base de dados. Imagine um eixo cartesiano x e y em que temos no eixo X visao computacional e no eixo Y diferentes arquiteturas como CNNs, RNNs etc... teriamos a segunda frase em um ponto mais proximo desse vetor criado na primeira frase que de uma terceira frase como "Transformers arquitetura" apesar de ter a palavra arquitetura elas possuem contextos diferentes seria como a palavra "colher" em duas frases significam coisas diferentes, "coloque a colher na boca" e "Frutas sao de colher" sao completamente distintas.

- RAG (Retrieval Augmented Generation)
 Conceito muito difundido na comunidade de LLM, que consiste em usar modelos pré-treinados para guiar a sua resposta com base em contextos passados no prompt base podendo guiar nao apenas os assuntos desejados mas como a llm respondera e o que pode ser dito ou nao evitando conteudo indesejado pelo desenvolvedor. Exemplo de um RAG simples, experimente perguntar a uma llm o que e cnn sem contexto, ela provavelmente falara do canal de televisao, mas passando o seguinte prompt a resposta mudara consideravelmente "Voce e um especialista de machine learning e tem o seguinte contexto, CNN sao arquiteturas de visao computacional responda a seguinte pergunta: O que e cnn?" vera que mudara substancialmente, a taxonomia do RAG consiste no seguinte -> papel desempenhado pela llm, contexto, conectivo ao pedido e o pedido final.

- Metodos http
 Sao metodos comums em sites http para fazer operacoes, sendo elas: GET, POST, PATCH, PUT DELETE. Cada uma delas faz algo diferente, get retorna o que foi pre definido na pagina, post posta algo na pagina e tem uma resposta, patch atualiza alguma informacao, put e utilizado para criar ou sustituir um recurso e delete para remover um dado desejado

- Docker, Dockerfile e Docker-compose
 Docker e o que faz o projeto ganhar vida, para que o projeto seja unificado em que virtualizamos apenas os recursos desejados para que evitemos problemas particulares de cada maquina. A base de docker e o Dockerfile que e o arquivo responsavel por criar a imagem e seus recursos vitais para serem orquestrados no docker-compose.yaml, no projeto vemos que temos um dockerfile voltado apenas as bibliotecas python com os requirements para funcionar o frontend, backend e airflow, para cada um desses em particular e feito um dockerfile para transferir os arquivos essenciais para rodar na virtualizacao e o comando para inicializar-los.

- Programacao orientada a objeto(POO ou OOP)(sem se estender)
 Paradigma de programacao utilizado focado no conceito de objetos, um objeto e algo que possui seus atributos e comportamentos(que chamaremos de metodos). Atributos sao no nosso caso tipos, por exemplo digamos que temos a classe carro e ele tem os seguintes atributos, velocidade atual,quantidade de gasolina, marca, cor etc... e seus comportamentos ou metodos sao acelerar, desacelerar e abastecer e quando instanciamos entao tornamos o objeto, podemos alterar sua construcao colocando os atributos desejados no momento e ir alterando de acordo com o decorrer do codigo. E uma classe pode ter seus filhos que herdam seus atributos e comportamentos mas podem haver mais atributos e comportamentos exemplo temos um SUV que herda de carro mas os atributos sao diferentes de outro filho como o esportivo e podem ter atributos diferentes como por exemplo tipo de combustivel ou outra diferenca que o desenvolvedor pensar.

## 2. O que é esse projeto e como ele coloca em pratica os conceitos citados?

Esse é um projeto que visa demonstrar algumas habilidades de MLOps com as seguinte stacks:

```
fastapi, chromadb, langchain, streamlit, httpx, airflow, pypdf2 e docker
```

O projeto utiliza o modelo gemini-2.0-flash visando demonstrar um projeto mlops simples,
demonstrando conceitos como vectordb, criacao de api com fastapi, uso do langchain para chamar
o modelo desejado, airflow para automatizar o rag baseado nos arquivos pdfs da pasta indicada 
no arquivo .env que deve ser criado pelo usuario seguindo as variaveis indicadas na secao 'COMO RODAR O PROJETO'

## 3. Como rodar o projeto

Primeiramente é necessário ter o arquivo .env na raiz do projeto com as variaveis indicadas, docker e docker compose instalado para que o projeto rode corretamente

### 3.1 Variaveis do arquivo .env
```
    API_KEY = 'sua_chave_google_ai_studio'
    PDF_PATH = 'path/para/os/documentos/pdf'
    AIRFLOW_USER = 'usuario_airflow'
    AIRFLOW_FIRSTNAME = 'primeiro_nome_airflow'
    AIRFLOW_LASTNAME = 'sobrenome_airflow'
    AIRFLOW_ROLE = 'Admin'
    AIRFLOW_PASSWORD = 'senha_desejada_para_o_airflow'
```

### 3.2 Comandos para rodar o projeto e como interagir com ele 

Apos definido o arquivo .env basta rodar o comando abaixo para que o docker rode em segundo plano no seu terminal.

```
docker compose up -d 
```

### 3.3 Como interagir com o projeto

Agora que o projeto esta rodando voce pode explorar-lo em 3 links diferentes rodando em sua maquina

- Aqui voce vai interagir com a llm do projeto colocando o contexto desejado baseado nos seus pdfs 
[Frontend da llm streamlit](http://localhost:8501)

- Aqui voce vera os esqueletos de cada endpoint do fastapi que o modelo esta utilizando para a llm 
[Endpoints da llm fastapi](http://localhost:8000)

- Aqui voce tera acesso a interface grafica do apache-airflow que orquestra automaticamente a leitura dos pdfs a cada 5 minutos e podera ver a execucao dele e diversas outras informacoes
[Orquestrador de leitor de pdfs](http://localhost:8080)

## 4. Aprendizado

Aqui podemos ver que foi necessario uma base solida de orientacao a objeto para uma organizacao do codigo visando refatoracao e adicionar features futuramente, o conhecimento mais teorico que foi utilizado foi o conceito de RAG, nele criamos um 'prompt' para que o modelo tenha um direcionamento para sua resposta, no contexto do projeto o RAG esta sendo utilizado para responder perguntas baseadas nos pdfs do seu computador como configurado, mas o RAG e mais poderoso ele pode alterar como o modelo respone e pode prevenir vazamento de informacoes de treino e prevenir alucinacoes e respostas com termos indesejados, tambem foi de extrema importancia saber fazer o backend chromadb que se utiliza dos conceitos de embedding para que facilite a utilizacao de queries baseado no conteudo da querie e sua implementacao e de extrema simplicidade poucas linhas de codigo e ja e criado a base de dados persistente no sistema operacional e mais algumas para adicionar items a essa base ou consultar-la, alem disso o conhecimento da abstracao langchain para chamada da api do google ai studio e a base de todo o projeto que sem ela nao teria a llm diretamente, uma alternativa seria utilizar diretamente as bibliotecas como transformers ou outras focadas em llms, mas quis aprender o langchain entao fiz o projeto tomando ele como base. Para utilizar o que foi feito no backend do chroma e o endpoint do fastapi foi feito necessario o uso da biblioteca httpx para fazer os requests aos endpoints, alem disso airflow foi utilizado para orquestrar a leitura dos pdfs periodicamente com o pypdf e embeddings do google chamado pelo langchain. Para o frontend do usuario foi feito utilizando streamlit. Por fim o projeto todo foi unificado com os dockerfiles em cada pasta para que rode igualmente em todas as maquinas instaladas com uma imagem unificada de python instalando os requirements do projeto e deixando unificado o comando de execucao dos arquivos de streamlit, fastapi e airflow. Assim o projeto se torna mais robusto e melhor compreensao para quem for rodar o projeto futuramente.