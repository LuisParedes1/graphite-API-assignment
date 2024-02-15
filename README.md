# Graphite Exercise

The following API takes as input parameters a URL and (optionally) limit. It then returns the terms with the highest TF-IDF on
the page according to the [all-the-news database](https://www.kaggle.com/snapcrack/all-the-news)

# Getting Started

Please download the [all-the-news database](https://www.kaggle.com/snapcrack/all-the-news) and extract the files.

Make sure `articles1.csv`, `articles2.csv` and `articles3.csv` are inside the "archive" folder because the program will look inside that folder to obtain the dataset to train the model.

## Installing Dependencies

This project was generated using fastapi framework.

Install dependencies from [requirements.txt](./requirements.txt) using

`pip install -r requirements.txt`

If you use Anaconda for environment management, you can recreate the environment using

`conda env create --file requirements.txt`

# Data Analysis

Inside of the [Jupyter Notebook](./DataAnalysis.ipynb) we do an inital data analysis to see what we are working with and check for any NaN values to clean.

To run the notebook:

- `conda activate [env]`
- `jupyter-notebook DataAnalysis.ipynb`
- Run the cells (cntl+enter)

# Execute the API

By default FastAPI uses address `http://127.0.0.1` and port `8000`

In the root directory, run `uvicorn main:app --reload`

This may take a minute because it trains the model each time the API is enabled.

When it's done the API will be enabled at the `http://127.0.0.1:8000` endpoint. By default it will redirect to the API Documentation Page.

## Open API Documentation in OpenAPI (Swagger)

You can find the API's documentation at `http://127.0.0.1:8000/docs`

# Tests

To run the tests please run from the root directory `python3 -m unittest test_*.py`

Remember to enable the endpoint before running integration tests.

# TF-IDF

To determine the TF-IDF for a given corpus D we use [sklearn's TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

Having `smooth_idf=True` (default value) TfidfVectorizer uses the following formulas

$$idf(t) = ln (\frac{N+1}{1+ df(t)}) + 1$$

where $N$ is the total number of documents in the document set and $df(t)$ is the document frequency of $t$; the document frequency is the number of documents in the document set that contain the term t.

$$tf(t,d) = f_{t,d}$$

where $f_{t,d}$ is the frequency of the term $t$ in the document $d$

And finally, for each term in each document

$$tfidf(t,d) = tf(t,d) \times idf(t)$$

# TfidfVectorizer Model

We train the TfidfVectorizer using the cleaned `all-the-news` dataset.

Using this model we then transform the new document (the url scaped document) and obtain its TF-IDF terms.

We ordered this terms in descending order and return the top `limit=10` terms as the API response.

# Further Improvements

To improve the results we can

- Manually implement a tokenizer that discards unintentional tokens (such as numerical tokens and symbols) but keeps intentional ones (for example U.S.A)
- Scrape from the new website header 2 and header 3 values (if available) and remove irrelevant aspects such as ads and maybe comments
- Use a larger training set
