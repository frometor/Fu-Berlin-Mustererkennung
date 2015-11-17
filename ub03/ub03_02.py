# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:02:42 2015

@author: florian and erik
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

#2_a)
mean1=(5,10)
covarianzmatrix1= [[1, 1], [1, 1]]

mean2=(5,5)
covarianzmatrix2=[[2,-1],[-1,2]]

mean3=(10,6)
covarianzmatrix3=[[0.1,0],[0,3]]


x1,y1 = np.random.multivariate_normal(mean1,covarianzmatrix1,100).T
x2,y2 = np.random.multivariate_normal(mean2,covarianzmatrix2,100).T
x3,y3 = np.random.multivariate_normal(mean3,covarianzmatrix3,100).T

plt.plot(x1,y1,'x',c='red')
plt.plot(x2,y2,'x',c='blue')
plt.plot(x3,y3,'x',c='black')

plt.show()

#2_b)
new_covarianzmatrix1 = np.cov(x1,y1)
new_covarianzmatrix2 = np.cov(x2,y2)
new_covarianzmatrix3 = np.cov(x3,y3)
print("new_covarianzmatrix1:")
print(new_covarianzmatrix1)
print("pearson-coefficient: "+ str(stats.pearsonr(x1,y1)[0])+"\n")
print("new_covarianzmatrix2:")
print(new_covarianzmatrix2)
print("pearson-coefficient: "+ str(stats.pearsonr(x2,y2)[0])+"\n")
print("new_covarianzmatrix3:")
print(new_covarianzmatrix3)
print("pearson-coefficient: "+ str(stats.pearsonr(x3,y3)[0])+"\n")

