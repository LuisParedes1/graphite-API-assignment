# Graphite Exercise

The following API takes as input parameters a URL and (optionally) limit. It then returns the terms with the highest TF-IDF on
the page according to the [all-the-news database](https://www.kaggle.com/snapcrack/all-the-news)

# Installing Dependencies

This project was generated using fastapi framework.

Install dependencies from requirements.txt using

`pip install -r requirements.txt`

If you use Anaconda for environment management, you can recreate the environment using

`conda env create --file requirements.txt`

# Data Analysis

Inside of the [Jupyter Notebook](./DataAnalysis.ipynb) we do an inital data analysis to see what we are working with and check for any NaN values.

We finish by concatenating all three datasets into a single one which we'll use for the project.

To run the notebook:

- conda activate (this will activate the base environment)
- jupyter-notebook DataAnalysis.ipynb
- Run the cells (cntl+enter)

# Execute the API

By default FastAPI uses address `http://127.0.0.1` and port `8000`

In the root directory, run `uvicorn main:app --reload`

This will enable the endpoint at `http://127.0.0.1:8000`

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
