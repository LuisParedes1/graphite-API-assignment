from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/tfidf")
def calculate_tfidf(url : str, limit : int = 1):
    return {"url": url, "limit": limit}