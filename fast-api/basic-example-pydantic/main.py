from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class ModelName(Enum):
    leonardo = "Leonardo"
    zeno = "Zeno"
    clipped = "Clipped"

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    user: ModelName

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    # print(item.name)
    # print(item.name.capitalize)
    # print(item.description)
    # print(item.description.capitalize)
    # return item
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Note que, mesmo pre-definindo os nomes de usuarios
# na Swagger UI nao ira mostrar as opces pre-definidas, pois sera convertido no JSON
# e dentro dela, estara snedo converitod em string
@app.post("/users/")
async def create_users(user: User):
    return user

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    # return {"item_id": item_id, **item.dict()}
    result = {"Item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
