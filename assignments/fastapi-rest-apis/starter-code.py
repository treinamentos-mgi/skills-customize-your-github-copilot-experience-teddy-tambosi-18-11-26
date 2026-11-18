# Código Inicial para a Tarefa de REST APIs com FastAPI
# Execute com: uvicorn starter-code:app --reload

from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "Livro: Python para Iniciantes", "price": 39.9},
    {"id": 2, "name": "Jogo da Forca", "price": 0.0},
    {"id": 3, "name": "Calculadora Científica", "price": 15.0},
]

# Tarefa 1: Criar a Primeira Rota GET
# Defina as rotas GET / e GET /items


# Tarefa 2: Receber Parâmetros de Caminho e de Consulta
# Defina GET /items/search (declare antes da rota com {item_id})
# Defina GET /items/{item_id}


# Tarefa 3: Criar Dados com POST e Validação com Pydantic
# Defina o modelo Item com BaseModel e a rota POST /items


# Tarefa 4: Implementar um CRUD Completo
# Defina PUT /items/{item_id} e DELETE /items/{item_id}
