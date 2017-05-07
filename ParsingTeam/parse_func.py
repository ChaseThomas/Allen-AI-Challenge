import json
import re
import nltk
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

def stopWordRemoval( wordList ):
    '''
    remove the stop words excluding not, no, and can't
    
    input: a list of string
    output: a list of string
    '''
    
    not_words = ["not", "no", "can't"]
    swords = nltk.corpus.stopwords.words('english')
    swords = [ w for w in swords if w not in not_words ]
    return [w for w in wordList if w not in swords ]

"""Returns lemmatized dataset"""
def lemmatize( wordList ):
    '''
    lemmatization
    
    input: a list of string
    output: a list of string
    '''
    return list(map(wnl.lemmatize, wordList))

def parse_func( wordList ):
    '''
    change to lowercase, remove stop words (excluding not, no, and can't), and lemmatization
    
    input: a list of string
    output: a list of string
    '''
    #make sure the words are lowercase
    
    wordList=[x.lower() for x in wordList]
    wordList=stopWordRemoval(wordList)
    wordList=lemmatize(wordList)
    return wordList