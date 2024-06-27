## Comandos Make

Para testar os endpoints da aplicação:

```bash

# Formatar o código de acordo com o ruff e o pylint
$ make format

# Iniciar os testes com pytest
$ make test

```

## Uso Opcional dos Comandos 'make'

### Descrição dos Comandos e Atalhos na Aplicação

## Makefile
- Comandos devem ser executados na raiz da aplicação.
- Sempre ative o ambiente virtual antes de usar os comandos.

### Definindo o Ambiente e Nome da Aplicação
- Primeiro, defina o tipo de ambiente e o nome da aplicação (APP_NAME) no terminal.
- Exemplo: 
  ```sh
  export FLASK_APP=project
  export FLASK_ENV=development
  ```

## Inicializar a Aplicação
- **Comando:** `make up`
  - Executa: `python -m project run` para inicializar a aplicação.

## Banco de Dados - Usando flask-migrate
- Após criar o modelo, inicialize a conexão com o banco de dados:
  1. **Inicializar o Banco de Dados**
     - **Comando:** `flask db init`
  2. **Criar a Instância SQLAlchemy**
     - **Comando:** `flask db migrate`
  3. **Criar Tabelas no Banco de Dados**
     - **Comando:** `flask db upgrade`

- **Comando:** `make db-init`
  - Executa: `flask db init` (Inicializa a instância SQLAlchemy)

- **Comando:** `make migrate`
  - Executa: `flask db migrate` (Executa as migrações das tabelas no banco de dados)

- **Comando:** `make upgrade`
  - Executa: `flask db upgrade` (Cria as tabelas no banco de dados)

## Configuração dos Ambientes (ENV e APP)

- **Comando:** `make env-default`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=default
    python -m project run
    ```

- **Comando:** `make env-development`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=development
    python -m project run
    ```

- **Comando:** `make env-testing`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=testing
    python -m project run
    ```

- **Comando:** `make env-production`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=production
    python -m project run
    ```
