import unittest 
import requests
import json

"""
    This tests require the endpoint to be enabled.

    Please run `uvicorn main:app --reload` before running this tests
"""

local_host = "http://127.0.0.1:8000"

class SimpleTest(unittest.TestCase):
    
    def test_given_valid_url_api_returns_valid_status_code(self):

        url="https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTf-idf"
        limit="10"

        response = requests.get(local_host+"/tfidf?url="+url+"&limit="+limit)
        
        self.assertEqual(response.status_code, 200)


    def test_given_valid_url_api_returns_tfidf_terms(self):

        url="https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTf-idf"
        limit="10"

        response = requests.get(local_host+"/tfidf?url="+url+"&limit="+limit)
        response_json = json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(len(response_json["terms"]), int(limit)) 


    def test_given_invalid_url_api_returns_invalid_status_code(self):
        
        url="invalid_url"
        limit="10"

        response = requests.get(local_host+"/tfidf?url="+url+"&limit="+limit)
        
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__': 
    unittest.main() 