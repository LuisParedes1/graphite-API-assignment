
import unittest 
from scrapper import scrape_url
from bs4 import BeautifulSoup


class SimpleTest(unittest.TestCase): 
  
    def test_scraper_returns_parsed_website_on_valid_url(self):
        url = "https://google.com"    
        parsed_website : str | None = scrape_url(url)     
        
        self.assertEqual(type(parsed_website), BeautifulSoup)

    
    def test_scrapper_returns_none_on_non_existant_url(self):
        url = "https://googles.com"
        parsed_website : str | None = scrape_url(url)
        
        self.assertEqual(parsed_website, None)

    # The following are variations of invalid urls
    def test_scrapper_returns_none_on_invalid_url_with_no_https(self):
        url = "googles.com"
        parsed_website : str | None = scrape_url(url)
        
        self.assertEqual(parsed_website, None)

    def test_scrapper_returns_none_on_invalid_url_with_htt(self):
        url = "htt://google.com"
        parsed_website : str | None = scrape_url(url)
        
        self.assertEqual(parsed_website, None)

    def test_scrapper_returns_none_on_invalid_url_format(self):
        url = "google"
        parsed_website : str | None = scrape_url(url)
        
        self.assertEqual(parsed_website, None)


if __name__ == '__main__': 
    unittest.main() 