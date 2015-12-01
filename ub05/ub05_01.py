# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 13:47:56 2015

@author: erik
"""

#%matplotlib inline

import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
# make plots bigger

plt.rcParams['figure.figsize'] = 16, 16  

#loadData
fishData = pd.read_csv("./fish.txt",delim_whitespace=True, dtype={'names': ('index', 'fish age', 'water temperature','fish length'),
                     'formats': ('i4','i4', 'i4','i4' )},index_col=0, names = [None, 'fish age', 'water temperature','fish length'])
fishData.head()

from sklearn.linear_model import LinearRegression
y= fishData['fish length']
features = ['water temperature','fish age']
x=fishData[features]
#print(x)
lm = LinearRegression()
lm.fit(x,y)

#print (lm.intercept_)
print (features[0],lm.coef_[0])
print (features[1],lm.coef_[1])

