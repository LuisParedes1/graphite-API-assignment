from fastapi import FastAPI
import pandas
from urllib.parse import unquote

app = FastAPI()
news_dataset = pandas.read_csv("all_the_news.csv")

@app.get("/tfidf")
def calculate_tfidf(url : str, limit : int = 10):

    # URLs can be received encoded. 
    # To be on the safe side, we decode into them into text
    decoded_url = unquote(url)

    return {
    "terms": [
            {
                "term": "term1",
                "tf-idf": 2.5
            },
            {
                "term": news_dataset["id"].unique().size,
                "tf-idf": 1
            },
            {
                "url":decoded_url
            }
        ]
    }