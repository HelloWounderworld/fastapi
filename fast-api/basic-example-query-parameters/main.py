from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# http://127.0.0.1:8000/items_op/foo?short=1
# http://127.0.0.1:8000/items_op/foo?short=True
# http://127.0.0.1:8000/items_op/foo?short=true
# http://127.0.0.1:8000/items_op/foo?short=on
# http://127.0.0.1:8000/items_op/foo?short=yes
@app.get("/items_op/{items_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        # return {"item_id": item_id, "q": q}
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    # return {"item_id": item_id}
    return item

# Note que, o que difere entre parametro de rota com o parametro de consulta
# esta em que o parametro de rota e obrigatorio fornecer uma entrada nela
# enquanto que no parametro de consulta, vc consegue forncer condicoes que
# o que torna opcional se vc atribui ou nao um parametro.
# Como podemos ver, no exemplo abaixo, no parametro de rota, mesmo colocando uma condicao de None,
# na tentativa de tornarmos ela opcional, ao verificarmos na aplicacao, http://127.0.0.1:8000/docs, nao os torna.
# Porem, na de consulta elas os torna.
@app.get("/params/{route_param}")
async def read_params(route_param: str | None = None, query_param: str | None = None):
    return {"route_param": route_param, "query_param": query_param}

# Caso vc queria tornar o parametro de consulta como um parametro obrigatorio
# Ou seja, bastaria nao colocar nenhum valor padrao ou uma opcao "ou"
# http://127.0.0.1:8000/items_req/foo-item -> Isso conduzira um erro, sem adicionar um parametro needy
# http://127.0.0.1:8000/items_req/foo-item/?needy=Leonardo
@app.get("/items_req/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

# Bom, podemos colocar mais de um parametro de rota, assim como, o mesmo, para o parametro de consulta
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})

    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    
    return item

@app.get("/items_mult/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
