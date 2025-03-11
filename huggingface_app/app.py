from fastapi import FastAPI
from fastapi import HTTPException  # 新增的导入语句

app = FastAPI()

@app.get("/")
def greet_json():
    return {"Hello": "World!"}
from fastapi import FastAPI
