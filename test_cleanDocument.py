import unittest 
from cleanDocument import cleanDocument

class SimpleTest(unittest.TestCase):
    
    def test_clean_doc_returns_same_clean_doc(self):

        doc = "what's up"

        clean_doc = cleanDocument(doc)
        
        self.assertEqual(clean_doc, "what's up")

    def test_removes_symbols_from_doc(self):

        doc = "what's up??"

        clean_doc = cleanDocument(doc)
        
        self.assertEqual(clean_doc, "what's up  ")

    def test_lowers_words_from_doc(self):

        doc = "WhAt's Up"

        clean_doc = cleanDocument(doc)
        
        self.assertEqual(clean_doc, "what's up")

    def test_stem_words_from_doc(self):

        doc = "i am running"

        clean_doc = cleanDocument(doc)
        
        self.assertEqual(clean_doc, "i am run")

    def test_lower_stem_removes_correctly_from_doc(self):

        doc = "I Am? running"

        clean_doc = cleanDocument(doc)
        
        self.assertEqual(clean_doc, "i am  run")

if __name__ == '__main__': 
    unittest.main() 