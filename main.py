from fastapi import FastAPI

app = FastAPI()

@app.get("/tfidf")
def calculate_tfidf(url : str, limit : int = 1):
    return {
    "terms": [
            {
                "term": "term1",
                "tf-idf": 2.5
            }
        ]
    }