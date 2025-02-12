from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/status")
def get_status():
    return {"status": "Running", "version": "1.0"}

@app.get("/echo/{text}")
def echo_text(text: str):
    return {"echo": text}
