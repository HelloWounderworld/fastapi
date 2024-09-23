from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

print(ModelName.alexnet)
print(ModelName.alexnet.value)
print()

print(ModelName.resnet)
print(ModelName.resnet.value)
print()

print(ModelName.lenet)
print(ModelName.lenet.value)
print()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    print(model_name)
    print(model_name.value)
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/models_str/{model_name_str}")
async def get_model(model_name_str: ModelName):
    print(model_name_str)
    print(model_name_str.value)
    if model_name_str is ModelName.alexnet:
        return model_name_str
    if model_name_str.value == "lenet":
        return model_name_str

    return model_name_str
