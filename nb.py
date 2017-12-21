# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn.naive_bayes import MultinomialNB
import pandas as pd 
import numpy as np

data = pd.read_csv('spambase.data').as_matrix()
# randomly shuffled data into train and test
np.random.shuffle(data)

X = data[:,:48]
Y = data[:,-1]

Xtrain = X[:-100,]
Ytrain = Y[:-100,]
Xtest = X[:-100,]
Ytest = Y[:-100,]

## Navie bayes
model = MultinomialNB()
model.fit(Xtrain,Ytrain)
print ("Classfication rate for NB:", model.score(Xtest, Ytest))

from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier()
model.fit(Xtrain,Ytrain)
print ("Classfication rate for AdaBoost:", model.score(Xtest, Ytest))









