from typing import Union

from fastapi import FastAPI

import logging
import datetime

logging.basicConfig(
    filename='../logs/logs-process.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info(f'Starting FastAPI Basic Example at {datetime.datetime.now()}')
app = FastAPI()

@app.get("/")
def read_root():
    logging.info(f'Processed "/" to get hello world at {datetime.datetime.now()}')
    return {"Hello": "Wounderworld!"}

@app.get("/items/{items_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    logging.info(f'Processed "/items" to get item_id: {item_id} and q: {q} at {datetime.datetime.now()}')
    return {"item_id": item_id, "q": q}