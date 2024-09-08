from typing import Union

from fastapi import FastAPI

import logging

logging.basicConfig(
    filename='../logs/logs-process.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info('Starting FastAPI Basic Example')
app = FastAPI()

@app.get("/")
def read_root():
    logging.info('Processed "/" to get hello world: {"Hello": "Wounderworld!"}')
    return {"Hello": "Wounderworld!"}

@app.get("/items/{items_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    logging.info(f'Processed "/items" to get item_id: {item_id} and q: {q}')
    return {"item_id": item_id, "q": q}