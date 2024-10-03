
# Gerenciamento de Alunos - API FastAPI

Esta é uma API simples de gerenciamento de alunos criada com [FastAPI](https://fastapi.tiangolo.com/).

## Funcionalidades

- **Criar Aluno**: Adiciona um novo aluno à lista.
- **Listar Alunos**: Exibe todos os alunos cadastrados.
- **Atualizar Aluno**: Atualiza as informações de um aluno existente.
- **Deletar Aluno**: Remove um aluno da lista.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instale fastAPI e uvicorn:
``` bash
pip install fastapi uvicorn
```

## Executando a Aplicação

Para rodar o servidor localmente, utilize o comando abaixo:
``` bash
uvicorn main:app --reload
```
Isso iniciará o servidor em ```http://127.0.0.1:8000```. Você poderá acessar a documentação automática da API gerada pelo Swagger em ```http://127.0.0.1:8000/docs```.



  



