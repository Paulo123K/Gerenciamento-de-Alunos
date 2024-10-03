from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()

class Aluno:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

alunos = [
    Aluno(id=1, nome="João Silva", email="joao.silva@email.com"),
    Aluno(id=2, nome="Maria Oliveira", email="maria.oliveira@email.com")
]

def aluno_para_dict(aluno: Aluno):
    return {
        "id": aluno.id,
        "nome": aluno.nome,
        "email": aluno.email
    }

@app.post("/alunos/")
def criar_aluno(id: int, nome: str, email: str):
    novo_aluno = Aluno(id=id, nome=nome, email=email)
    alunos.append(novo_aluno)
    return aluno_para_dict(novo_aluno)

@app.get("/alunos/")
def listar_alunos():
    return [{"id": aluno.id, "nome": aluno.nome, "email": aluno.email} for aluno in alunos]

@app.put("/alunos/{aluno_id}")
def atualizar_aluno(aluno_id: int, nome: str, email: str):
    for aluno in alunos:
        if aluno.id == aluno_id:
            aluno.nome = nome
            aluno.email = email
            return aluno_para_dict(aluno)
    raise HTTPException(status_code=404, detail="Aluno não encontrado")

@app.delete("/alunos/{aluno_id}")
def deletar_aluno(aluno_id: int):
    global alunos
    alunos = [aluno for aluno in alunos if aluno.id != aluno_id]
    return {"message": "Aluno deletado com sucesso"}
