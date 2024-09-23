from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class ModelPath(Enum):
    path_example = "home/leonardo/myfile.txt"
    path_example2 = "home/cobaia/myfile.txt"
    empty_path = ""

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/paths/{complete_path:path}")
async def read_path(model_path: ModelPath):
    print(model_path)
    print(model_path.value)
    if model_path is ModelPath.path_example:
        return "/paths/" + model_path.value
    if model_path.value == "home/cobaia/myfile.txt":
        return "/paths/" + model_path.value
    
    return "No one path defined..."
