from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas
from cleanDocument import cleanDocument

# precondition: Receive a BeautifulSoup class which contains the parsed website
# postcondition: Returns a clean document to use in the transform
def preprocessDocument(parsed_website:BeautifulSoup):
    
    title = parsed_website.find('h1')

    if title:
        title = title.get_text()
    else:
        title = ""

    paragraphs = parsed_website.find_all('p')

    title_and_content = title + ' ' + ' '.join([p.get_text() for p in paragraphs])

    return cleanDocument(title_and_content)

# For step by step in traning the model, see DataAnalysis.ipynb
# postcondition: Returns the tf-idf model
def trainModel():

    articles1 = pandas.read_csv("./archive/articles1.csv")
    articles2 = pandas.read_csv("./archive/articles2.csv")
    articles3 = pandas.read_csv("./archive/articles3.csv")

    concat_dataset = pandas.concat([articles1, articles2, articles3], ignore_index=True)
    concat_dataset['title_and_content'] = concat_dataset['title'] + " " + concat_dataset['content']

    concat_dataset.loc[64875,"title_and_content"] = concat_dataset.loc[64875,"content"]
    concat_dataset.loc[120637,"title_and_content"] = concat_dataset.loc[120637,"content"]

    train_dataset = concat_dataset[["id", "title_and_content"]]

    train_dataset.loc[:,"title_and_content"] = train_dataset["title_and_content"].apply(cleanDocument)

    corpus = train_dataset["title_and_content"].to_list()

    tfidf_vectorizer = TfidfVectorizer(stop_words="english", lowercase=True, strip_accents='unicode')

    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

    return tfidf_vectorizer
    