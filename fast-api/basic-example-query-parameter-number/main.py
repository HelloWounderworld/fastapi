from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),
    q: str | None = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/itemsrobust/{item_id}")
async def read_items_robust(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# kwargs - https://github.com/HelloWounderworld/Review-Python/blob/main/Revisao-Udemy/secao04-Python-Intermediario-Funcoes-Dicionario-Modulos-Programcao-Funcional-e-mais/README.md#aula-32---empacotamento-e-desempacotamento-de-dicion%C3%A1rios--args-e-kwargs
@app.get("/itemskwargs/{item_id}")
async def read_items_kwargs(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Putting order "ge" (greater than)
@app.get("/itemsorders/{item_id}")
async def read_items_orders(
    *, item_id: int = Path(title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# ge - greater than
# le - less than
@app.get("/itemsinterval/{item_id}")
async def read_items_interval(
    *,
    item_id: int = Path(title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
