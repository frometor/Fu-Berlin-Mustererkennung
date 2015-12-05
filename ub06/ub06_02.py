# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:48:38 2015

@author: erik
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.lda import LDA

#loadData
fisherData = pd.read_csv("./fisher.txt",delimiter=",", dtype={'names': ('X', 'Y','theClass'),\
'formats': ('i4','i4', 'i4')},index_col=False, names = ['x', 'y','theClass'])
fisherData.head()

allx=fisherData['x']
ally=fisherData['y']
theClass=fisherData['theClass']
xandy = ['x','y']
theXandY = fisherData[xandy]

x0=[]
x1=[]
y0=[]
y1=[]

for i in range(len(fisherData)):
    if (theClass[i]==0):
        x0.append(allx[i])
    if (theClass[i]==1):
      x1.append(allx[i])

for j in range(len(fisherData)):
    if (theClass[j]==0):
        y0.append(ally[j])
    if (theClass[j]==1):
      y1.append(ally[j])        

fisherX=np.array(theXandY)
fisherClass=np.array(theClass)
clf=LDA()
fisher=clf.fit(fisherX,fisherClass) 
print(fisher)
       
#plt.plot (x0,y0,'ro')

#plt.plot (x1,y1,'^g')
#plt.show()

