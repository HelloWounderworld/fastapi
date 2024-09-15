from typing import Union

from fastapi import FastAPI

app = FastAPI()

# Você só pode usar await dentro de funções criadas com async def.
@app.get("/")
async def read_root():
    return {"Hello": "Wounderworld!"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}