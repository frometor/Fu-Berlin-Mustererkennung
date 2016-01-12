# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:21:21 2016

@author: florian
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#==============================================================================
# global_variables
#==============================================================================
iterations = 1000
wahrscheinlichkeitGrenze = 0.01
beta0 , beta1 = np.array([-100,100]) , np.array([-100,100])
betarange = np.arange(beta0[0],beta0[1],1)
#==============================================================================
# function
#==============================================================================
def probability(x,beta):
    return (np.exp(np.dot(beta.T,x)) / (1+ np.exp(np.dot(beta.T,x))))

def nabla(x,y,beta):
    summ = np.zeros(len(beta))
    for i in range(len(x)):
        if(y[i]):
            if(probability(x[i],beta) < wahrscheinlichkeitGrenze):
                summ -= np.dot(x[i],(y[i] - probability(x[i],beta)))
            else:
                summ += np.dot(x[i],(y[i] - probability(x[i],beta)))
        else:
            if(1 - probability(x[i],beta > wahrscheinlichkeitGrenze)):
                summ += np.dot(x[i],(y[i] - probability(x[i],beta)))
            else:
                summ -= np.dot(x[i],(y[i] - probability(x[i],beta)))
    return summ
    

def gradientDescent(x,y,beta,alpha):
#    pltrangeX = np.arange(0,1.1,0.01)          
    for i in range(iterations):
#        if (i == 0 or i == 10 or i == 100 or i == iterations-1 ):     
#            pltrangeY = []
#            for j in range(len(pltrangeX)):
#                pltrangeY.append(probability((1,pltrangeX[j]),beta))
#            plt.plot(pltrangeX,pltrangeY)
        speicher = nabla(x,y,beta)
        beta =  beta + np.dot(alpha,speicher) 
    return beta
        
def logLikelyhood(x,y,beta):
    speicher1,speicher2 = 0,0
    for i in range(len(x)):
        speicher1 += np.dot(y[i],np.dot(beta.T,x[i]))
        speicher2 += np.log(1+ np.exp(np.dot(beta.T,x[i])))
    return speicher1 - speicher2
#==============================================================================
# main
#==============================================================================
spiders = np.genfromtxt('spiders.txt',delimiter=",")
data,sand, isSpider = [],[],[]

for row in spiders:
    sand.append(row[0])
    isSpider.append(row[1])
    data.append((1,row[0]))
beta = np.zeros(len(data[0]))
  
#plt.plot(sand,isSpider,'ro')

beta =  gradientDescent(data,isSpider,beta,0.1)
print ("beta", beta)
print ("Log-Likelyhood Spiders: ", logLikelyhood(data,isSpider,beta)+1)
print ("Log-Likelyhood beta0: ", logLikelyhood(data,isSpider,beta0))


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
X,Y = np.meshgrid(betarange,betarange)
zs = np.array([logLikelyhood(data,isSpider,np.array([x,y])) for x,y in zip(np.ravel(X),np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_wireframe(X,Y,Z,rstride=10,cstride=10)
ax.scatter(beta[0],beta[1],logLikelyhood(data,isSpider,beta),c="red",marker="o", s=50)
#==============================================================================
#  __plot-configs__
#==============================================================================
#plt.xlim(0.2,1.1)
#plt.ylim(-0.1,1.1)
ax.set_xlim3d(-100,100)
ax.set_ylim3d(-100,100)


plt.savefig("3D_spiders_plot.png")
plt.show()