# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:48:38 2015

@author: erik
"""
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import itertools as it

wine = pd.read_csv("./winequality-red.txt", delimiter=";",
dtype={'names':('fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality'),
'formats':('i4','i4','i4','i4','i4','i4','i4','i4','i4','i4','i4','i4','i4')},
index_col=False,
names=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality'])
#wine.head(n=5)
qual=wine['quality']
#print(qual)

features=['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']

iters= list(it.combinations(features,1))
#print('iters',iters)


feat=wine[iters[0][0]]

#print('feat',feat)


lm = LinearRegression()

tmp = []
for i in feat:
    tmp.append([i])
    
lm.fit(tmp,qual)
prediction = lm.predict(tmp)
p = sum(np.square(qual-prediction))
plt.scatter(1,p)
plt.show()




#print (lm.intercept_)
print (lm.coef_)