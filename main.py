from fastapi import FastAPI
import pandas

app = FastAPI()
news_dataset = pandas.read_csv("all_the_news.csv")

@app.get("/tfidf")
def calculate_tfidf(url : str, limit : int = 10):
    return {
    "terms": [
            {
                "term": "term1",
                "tf-idf": 2.5
            },
            {
                "term": news_dataset["id"].unique().size,
                "tf-idf": 1
            }
        ]
    }