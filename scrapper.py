import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

# URLs can be received encoded. To be on the safe side, we decode into them into text
def scrape_url(url:str):

    response = requests.get(unquote(url))

    if(response.status_code != 200):
        return None
        
    soup = BeautifulSoup(response.content, "html.parser")

    title = soup.find('h1')

    if title:
        title = title.get_text()
    else:
        title = ""

    paragraphs = soup.find_all('p')
    all_text = title + ' ' + ' '.join([p.get_text() for p in paragraphs])

    return all_text.replace('\n', '').replace('\t', '')