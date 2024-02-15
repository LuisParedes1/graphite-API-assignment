from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import starlette.status as status
from scrapper import scrape_url
from utils import preprocessDocument, trainModel

app = FastAPI()

# Train model when the API starts
tfidf_model = trainModel()

@app.get("/tfidf", 
         description="""This endpoint takes a URL and returns the 
            terms with the highest TF-IDF on the page.""", 
         summary="The pages' top terms with the highest TF-IDF")
def calculate_tfidf(url : str, limit : int = 10):

    parsed_website : str | None = scrape_url(url)
    
    if (parsed_website is None):
        raise HTTPException(status_code=404, detail="URL not found")
    
    scraped_document = preprocessDocument(parsed_website)

    tfidf_url_page = tfidf_model.transform([scraped_document]).toarray()[0]

    ordered_tfidf_url_page = sorted( zip(tfidf_model.get_feature_names_out(), tfidf_url_page), 
                                    key=lambda x: x[1], reverse=True )
    
    return {
        "terms": [
            {
                "term": term,
                "tf-idf": tfidf
            } for term, tfidf in ordered_tfidf_url_page[:limit]
        ]
    }

@app.get("/" , include_in_schema=False)
def main():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)