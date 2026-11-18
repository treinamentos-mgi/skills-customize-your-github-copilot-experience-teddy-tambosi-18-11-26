# 📘 Assignment: Building REST APIs com FastAPI

## 🎯 Objetivo

Aprenda a criar uma API REST com FastAPI, definindo rotas, recebendo dados do cliente, validando informações com Pydantic e retornando respostas com os códigos HTTP corretos.

## 📝 Tarefas

### 🛠️ Criar a Primeira Rota GET

#### Descrição
Crie uma aplicação FastAPI com uma rota `GET /` que retorna uma mensagem de boas-vindas e uma rota `GET /items` que retorna uma lista de itens (por exemplo, uma lista de livros ou jogos).

Para executar a API, instale as dependências com `pip install fastapi uvicorn` e rode `uvicorn starter-code:app --reload`. Depois, acesse `http://127.0.0.1:8000/docs` para ver a documentação gerada automaticamente.

#### Requisitos
O programa concluído deve:

- Criar uma instância de `FastAPI` chamada `app`
- Definir a rota `GET /` retornando um dicionário com a chave `"message"`
- Definir a rota `GET /items` retornando uma lista de pelo menos 3 itens
- Verificar que as duas rotas aparecem na página `/docs`

### 🛠️ Receber Parâmetros de Caminho e de Consulta

#### Descrição
Crie a rota `GET /items/{item_id}` que retorna um item pelo seu identificador e a rota `GET /items/search` que filtra os itens pelo nome, usando um parâmetro de consulta opcional `q`.

Atenção: declare `/items/search` antes de `/items/{item_id}`, senão o FastAPI tentará interpretar `"search"` como um `item_id`.

#### Requisitos
O programa concluído deve:

- Definir `GET /items/{item_id}` com `item_id` do tipo `int`
- Retornar o item correspondente, ou um erro HTTP 404 quando o `item_id` não existir
- Definir `GET /items/search` com o parâmetro opcional `q` (`str | None`)
- Retornar apenas os itens cujo nome contém o texto de `q`; sem `q`, retornar todos os itens

```
GET /items/2           -> {"id": 2, "name": "Jogo da Forca", "price": 0.0}
GET /items/search?q=jo -> lista com os itens cujo nome contém "jo"
GET /items/99          -> 404 Not Found
```

### 🛠️ Criar Dados com POST e Validação com Pydantic

#### Descrição
Crie um modelo Pydantic chamado `Item` com os campos `name`, `price` e `available`. Em seguida, crie a rota `POST /items` que recebe um item no corpo da requisição (JSON), gera um novo `id` e o adiciona à lista.

#### Requisitos
O programa concluído deve:

- Definir a classe `Item` herdando de `BaseModel`, com `name: str`, `price: float` e `available: bool = True`
- Definir `POST /items` que recebe um `Item` e retorna o item criado com o `id` gerado
- Responder com o status HTTP `201 Created`
- Rejeitar automaticamente, com erro `422`, requisições em que `price` não seja um número (teste pelo `/docs`)

```
POST /items
{"name": "Xadrez", "price": 25.5}

-> 201 Created
{"id": 4, "name": "Xadrez", "price": 25.5, "available": true}
```

### 🛠️ Implementar um CRUD Completo

#### Descrição
Complete a API com as operações de atualização e remoção, mantendo os dados em memória (em uma lista ou dicionário). Use o mesmo modelo `Item` para validar as atualizações.

#### Requisitos
O programa concluído deve:

- Definir `PUT /items/{item_id}` que substitui os dados de um item existente
- Definir `DELETE /items/{item_id}` que remove um item e retorna uma mensagem de confirmação
- Retornar 404 em `PUT` e `DELETE` quando o item não existir
- Testar todas as rotas (GET, POST, PUT e DELETE) pelo `/docs` e confirmar que a lista de itens reflete as alterações
