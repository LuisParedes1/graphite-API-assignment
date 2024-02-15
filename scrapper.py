import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

# precondition: URLs can be received encoded. To be on the safe side, we decode into them into text
# postcondition: Returns the parsed website or None if there's any error 
def scrape_url(url:str):

    try:
        response = requests.get(unquote(url))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return None
        
    return BeautifulSoup(response.content, "html.parser")