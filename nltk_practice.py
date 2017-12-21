# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:43:51 2017

@author: WB479AQ
"""

import nltk
# words tags 
print(nltk.pos_tag("Machine learning is great".split()))

# stemming and lemmatization, reduce words to a "base" form
# stemming is more "crude"
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
print(porter_stemmer.stem('wolves'))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('wolves'))

# NER(Named entity recognition)
s = 'Albert Einstein was born on March 14, 1879'
tags = nltk.pos_tag(s.split())
print(tags)

nltk.ne_chunk(tags).draw()

######################### synonymy and polysemy (one word with mutiple meanings)
# PCA does 3 things: 
# 1) decorrelates input data; 2) Transformed data is ordered by information content; 3) Dimensionality reduction
# * denosing/smoothing/improving generalization



















