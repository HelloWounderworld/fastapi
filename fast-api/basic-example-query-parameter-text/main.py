from typing import Union, List

from fastapi import FastAPI, Query

app = FastAPI()

# expressoes regulares: pattern
@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50, pattern="^fixedquery$")):
    results = { "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})

    return results

# Uma outra maneira de tornar um valor algo opcional, alem de definir o None, seria definir um valor padrao.
# Ou seja, generalizando, para que um parametro de consulta seja opcional seria mdiante a um valor padrao definido
@app.get("/defaultvalor")
async def read_defaultvalor(q: str = Query(default="fixedquery", min_length=3)):
    results = { "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})

    return results

@app.get("/ellipsis")
async def read_ellipsis(q: str = Query(...,min_length=3)):
    results = { "items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})

    return results

# http://localhost:8000/lists/?q=foo&q=bar
# http://127.0.0.1:8000/lists/?q=Leonardo&q=Teramatsu&q=Clipped&q=Person
@app.get("/lists/")
async def read_lists(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items

@app.get("/justlist/")
async def read_items(q: List[str] = Query(default=["foo", "bar"])):
    query_items = {"q": q}
    return query_items

# Neste caso, a unica coisa que difere, seria que a forma abaixo nao ira ocorrer alguma validacao dos conteudos dentro dessa lista
# Emvez de colocar algo como, List[int], onde sera validado se os conteudos dentro da lista sao inteiros.
@app.get("/withouttyping/")
async def read_items(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items

@app.get("/withtitle/")
async def read_items(
    q: Union[str, None] = Query(default=None, title="Query string", min_length=3),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/produtossemtitutlo/")
async def listar_produtos_sem_titulo(
    categoria: str = Query(..., min_length=3),
    limite: int = Query(10, gt=0)
):
    return {"categoria": categoria, "limite": limite}

@app.get("/produtoscomtitulo/")
async def listar_produtos_com_titulo(
    categoria: str = Query(..., title="Categoria do Produto", min_length=3),
    limite: int = Query(10, title="Número Máximo de Produtos", gt=0)
):
    return {"categoria": categoria, "limite": limite}

@app.get("/itemsdescription/")
async def read_items_description(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Apelidando/Dando nomes aos parametros de consulta
# http://127.0.0.1:8000/items_nickname/?item-query=Leo
# De forma direta, vc nao poderia passar "item-query" como parametro. O correto seria "item_query".
@app.get("/items_nickname/")
async def read_items_nickname(q: Union[str, None] = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Parametro que sera descontinuado.
# Maneiras que vc poderia utilizar para lembrar, enquanto estiver sendo usado, ate que seja descontinuado.
@app.get("/items_deprecated/")
async def read_items_deprecated(
    q: Union[str, None] = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        pattern="^fixedquery$",
        deprecated=True,
    ),
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
