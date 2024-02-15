from bs4 import BeautifulSoup

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


def cleanDocument(document:str):
    return document.replace('\n', '').replace('\t', '').lower()