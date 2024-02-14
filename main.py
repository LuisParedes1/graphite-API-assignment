from fastapi import FastAPI
import pandas

from scrapper import scrape_url
from sklearn.feature_extraction.text import TfidfVectorizer


app = FastAPI()
news_dataset = pandas.read_csv("all_the_news.csv")


@app.get("/tfidf")
def calculate_tfidf(url : str, limit : int = 10):

    scraped_text : str | None = scrape_url(url)
    
    if (scraped_text is None):
        return{
            "Error":"500" 
        }

    documents = news_dataset["title_and_content"].to_list()
    documents.append(scraped_text)

    tfidf = TfidfVectorizer(stop_words="english", lowercase=True, strip_accents='unicode')

    # get tf-df values
    result = tfidf.fit_transform(documents)

    tfidf_ordered = sorted(zip(tfidf.get_feature_names_out(), result[-1].toarray()[0]), key=lambda x: x[1], reverse=True)
    
    return {
        "terms": [
            {
                "term": term,
                "tf-idf": tfidf
            } for term, tfidf in tfidf_ordered[:limit]
        ]
    }