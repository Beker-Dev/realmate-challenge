# Realmate-Challenge

Este repositório contém um projeto Python/Django. Siga as instruções abaixo para configurar e executar o projeto localmente.


## Instruções para iniciar o projeto

### Utilizando docker

#### Requisitos

* Docker instalado

#### Instruções

* Execute o arquivo `docker-compose`:

`docker-compose up -d --build`

### Sem utilização do docker

#### Requisitos

* Python 3.x instalado

* pip instalado

* Configuração do ambiente

#### Instruções

* Crie e ative um ambiente virtual:

`python -m venv venv`

*Ative o ambiente virtual

`.\venv\Scripts\activate`

* Instale o Poetry:

`pip install poetry`

* Instale as dependências do projeto:

`poetry install`

### Executando o projeto

* Aplique as migrações ao banco de dados:

`python manage.py migrate`

* Colete arquivos estáticos:

`python manage.py collectstatic --noinput`

* Inicie o servidor de desenvolvimento:

`python manage.py runserver`

Agora o projeto estará rodando em http://127.0.0.1:8000/. Acesse no navegador para conferir.
