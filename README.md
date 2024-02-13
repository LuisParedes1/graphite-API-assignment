# Graphite Exercise

The following API takes as input parameters a URL and limit. It then returns the terms with the highest TF-IDF on
the page according to the [all-the-news database](https://www.kaggle.com/snapcrack/all-the-news)

# Data Analysis

Inside of the [Jupyter Notebook](./DataAnalysis.ipynb) we do an inital data analysis to see what we are working with and check for any NaN values.

We finish by concatenating all three datasets into a single one which we'll use for the project.

To run the notebook:

- conda activate (this will activate the base environment)
- jupyter-notebook DataAnalysis.ipynb
- Install pandas with `!pip install pandas`
- Run the cells (cntl+enter)

# Installing Dependencies

This project was generated using fastapi framework.

Install dependencies from requirements.txt using

`pip install -r requirements.txt`

If you use Anaconda for environment management, you can recreate the environment using

`conda env create --file requirements.txt`

## Execute the API

By default FastAPI uses address `127.0.0.1` and port `8000`

In the root directory, run `uvicorn main:app --reload`

This will enable the endpoint at `http://127.0.0.1:8000`

# Open API Documentation in OpenAPI (Swagger)

You can find the API's documentation at `http://127.0.0.1:8000/docs`
