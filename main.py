from fastapi import FastAPI, HTTPException
import pandas

from scrapper import scrape_url
from sklearn.feature_extraction.text import TfidfVectorizer


app = FastAPI()
news_dataset = pandas.read_csv("all_the_news.csv")


@app.get("/tfidf")
def calculate_tfidf(url : str, limit : int = 10):

    scraped_text : str | None = scrape_url(url)
    
    if (scraped_text is None):
        raise HTTPException(status_code=404, detail="URL not found")

    # Get corpus for the TF-IDF
    corpus = news_dataset["title_and_content"].to_list()
    corpus.append(scraped_text)

    tfidf = TfidfVectorizer(stop_words="english", lowercase=True, strip_accents='unicode')

    # get tf-df values for every document
    result = tfidf.fit_transform(corpus)

    # get the TF-IDF values on the url page.
    tfidf_url_page = result[-1].toarray()[0]

    # Order the page's TF-IDF in descending order
    # We save it in (term, tf-idf) tuple
    ordered_tfidf_url_page = sorted(zip(tfidf.get_feature_names_out(), tfidf_url_page), key=lambda x: x[1], reverse=True)
    
    return {
        "terms": [
            {
                "term": term,
                "tf-idf": tfidf
            } for term, tfidf in ordered_tfidf_url_page[:limit]
        ]
    }