from fastapi import FastAPI
from utils import sentiment_router

app = FastAPI()

app.include_router(sentiment_router, prefix="/api", tags=["sentiment"])

@app.get("/")
def say_hello():
    return {"message": "Hello, World!"}

