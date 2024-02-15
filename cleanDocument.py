from nltk.stem import PorterStemmer

def removeSymbols(data:str):
    symbols = "!\"#$%&()*+-./:;<=>?@[\\]^_`{|}~\n\t“”—"
    
    for i in symbols:
        data = data.replace(i, ' ')
    
    return data

def lowerWords(data:str):
    return data.lower()

def stemWords(data:str):
    return PorterStemmer().stem(data)

# postcondition: Returns a clean document.
def cleanDocument(document:str):
    document = lowerWords(document)
    document = removeSymbols(document)
    document = stemWords(document)
    return document