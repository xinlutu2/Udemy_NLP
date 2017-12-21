# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:18:56 2017

@author: WB479AQ
"""

import nltk 
import random
import numpy as np

from bs4 import BeautifulSoup

positive_reviews = BeautifulSoup(open('positive.review.xml').read(),'xml')
positive_reviews = positive_reviews.findAll('review_text')

#print(positive_reviews)

# extract trigrams and insert into dictionary
# (w1, w3) is the key, [ w2 ] are the values
trigrams = {}
for review in positive_reviews:
    s = review.text.lower()
    tokens = nltk.tokenize.word_tokenize(s)
    for i in range(len(tokens) - 2):
        k = (tokens[i], tokens[i+2])
        if k not in trigrams:
            trigrams[k] = []
        trigrams[k].append(tokens[i+1])
        
trigrams_probabilities = {}
for k,words in trigrams.items(): ## python 3 rename dict.iteritems() to dict.items()
    if len(set(words)) > 1:
        d = {}
        n = 0
        for w in words:
            if w not in d:
                d[w] = 0
            d[w] += 1
            n += 1
        for w,c in d.items():
            d[w] = float(c) / n
        trigrams_probabilities[k] = d
      
def random_sample(d):
    # choose a random sample from dictionary where values are the probabilities
    r = random.random()
    cumulative = 0
    for w, p in d.items():
        cumulative += p
        if r < cumulative:
            return w


def test_spinner():
    review = random.choice(positive_reviews)
    s = review.text.lower()
    print("Original:", s)
    tokens = nltk.tokenize.word_tokenize(s)
    for i in range(len(tokens) - 2):
        if random.random() < 0.2: # 20% chance of replacement
            k = (tokens[i], tokens[i+2])
            if k in trigrams_probabilities:
                w = random_sample(trigrams_probabilities[k])
                tokens[i+1] = w
    print("Spun:")
    print(" ".join(tokens).replace(" .", ".").replace(" '", "'").replace(" ,", ",").replace("$ ", "$").replace(" !", "!"))       
        
test_spinner()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        