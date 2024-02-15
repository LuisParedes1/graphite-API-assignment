from fastapi import FastAPI, HTTPException

from scrapper import scrape_url
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


app = FastAPI()

# Loading the trained model when the API starts
tfidf_model = pickle.load(open("tfidf_vectorizer_model.joblib", 'rb'))

@app.get("/tfidf")
def calculate_tfidf(url : str, limit : int = 10):

    scraped_document : str | None = scrape_url(url)
    
    if (scraped_document is None):
        raise HTTPException(status_code=404, detail="URL not found")
    

    tfidf_url_page = tfidf_model.transform([scraped_document]).toarray()[0]

    ordered_tfidf_url_page = sorted(zip(tfidf_model.get_feature_names_out(),
                                    tfidf_url_page), key=lambda x: x[1], reverse=True )
    
    return {
        "terms": [
            {
                "term": term,
                "tf-idf": tfidf
            } for term, tfidf in ordered_tfidf_url_page[:limit]
        ]
    }