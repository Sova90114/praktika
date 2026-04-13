from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "Version": os.getenv("APP_VERSION", "dev")}
