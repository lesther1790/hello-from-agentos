
from fastapi import FastAPI

app = FastAPI()

API_VERSION = "1.0.0"

@app.get("/")
def root():
    return {"hello": "agentos"}

@app.get("/version")
def version():
    return {"version": API_VERSION}
