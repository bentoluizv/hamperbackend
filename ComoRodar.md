
# Delivery App Backend

backend do projeto Delivery App. 

## Pré-requisitos

- Python 3.11.9 ou inferior
- Docker & Docker compose

## Configuração do Ambiente

1. Crie um ambiente virtual utilizando o módulo `venv` do Python. Recomendamos nomear o ambiente como `venv` para que seja ignorado pelo Git:

```bash
python3 -m venv venv
```

2. Ative o ambiente virtual:

```bash
source venv/bin/activate
```

3. Instale as dependências necessárias utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Após seguir esses passos, seu ambiente estará pronto para executar o projeto.

## Configuração do Projeto

1. Renomeie o arquivo `.secrets-example.toml` para `.secrets.toml`. Este arquivo contém as variáveis de ambiente necessárias para o Flask.

2. Defina as variáveis de ambiente para o Flask:

```bash
export FLASK_APP=project
export FLASK_ENV=exemplo
```

Substitua `exemplo` pelo ambiente em que você deseja executar o projeto (por exemplo, `development`, `testing`, `production`).


## Configuração do Banco

1. Execute o seguinte comando para iniciar o banco de dados fornecido pelo Docker:

```bash
docker compose up
```

2. Agora, inicialize o banco de dados, crie a instância do SQLAlchemy e crie as tabelas no banco de dados:


```bash
flask db init # executamos 1 vez pois serve para inicializar a conexão
flask db migrate # executamos para criar a instancia do sqlalchemy
flask db upgrade # executamos para criar as tabelas no banco
```

## Executando o Projeto

Inicializa a aplicação:
```bash
make up
```

## Swagger

Para acessar a documentação da API, acesse o seguinte link: [http://127.0.0.1:5000/api/v1](http://127.0.0.1:5000/api/v1). Lá você encontrará a versão do Swagger funcionando!
