from typing import Union

from fastapi import FastAPI

app = FastAPI()

# Você só pode usar await dentro de funções criadas com async def.
@app.get("/")
async def read_root():
    return {"Hello": "Wounderworld!"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: Union[int, None] = None, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the_current_user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
