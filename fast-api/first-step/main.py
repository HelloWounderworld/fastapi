from fastapi import FastAPI

app = FastAPI()

@app.get("/asynchronous")
async def root():
    return {"message": "Hello Wounderworld!"}

@app.get("/sequential")
def root():
    return {"message": "Hello Wounderworld!"}

@app.get("/items/{items_id}")
async def read_item(item_id: int | float):
    return {"item_id": item_id}
