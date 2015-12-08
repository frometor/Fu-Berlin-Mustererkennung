# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:48:38 2015

@author: erik
"""
import matplotlib.pyplot as plt
import numpy as np

# perceptron-algorithem with x iterations
def perceptron(xyClass,belongingClass):
    k = 0    
    x = 1000000
    w = np.zeros(len(xyClass[0])) # len of one row
    while k < x:
        random = np.random.randint(0,len(xyClass))
        randomVector = xyClass[random]
        randomBelongingClass = belongingClass[random]
        if (randomBelongingClass):
            w,k = perceptonPositiv(w,randomVector,k)
        else:
            w,k = perceptonNegativ(w,randomVector,k)
    return w
    
    
def perceptonPositiv(w,x,k):
    if(w.dot(x) >= 0):
        return w,k
    else:
        return w + x ,k+1

def perceptonNegativ(w,x,k):        
    if (w.dot < 0):
        return w,k
    else:        
        return w - x, k+1
    
    
def normalize(vector):
    sum = 0    
    for x in vector:
        sum += np.abs(x)
    return vector / np.sqrt(sum) 
#----------------------------- main -----------------------------
    
# loadData
csv = np.genfromtxt('fisher.txt',delimiter=",")
x0 = []
x1 = []
y0 = []
y1 = []
allClass0,allClass1 = [],[]
allxy,allClass = [],[]
x0_P,y0_P,x1_P,y1_P = [],[],[],[]

for row in csv:
    if (row[2]):
        x0.append(row[0])
        y0.append(row[1])
        allClass0.append((row[0],row[1]))
    else:
        x1.append(row[0])
        y1.append(row[1])
        allClass1.append((row[0],row[1]))
    allxy.append((row[0],row[1]))
    allClass.append(row[2])

# plot all points    
plt.plot (x0,y0,'ro')
plt.plot (x1,y1,'^g')

# compute and plot the mean
mean0 = np.mean((x0,y0),axis=1)
mean1 = np.mean((x1,y1),axis=1)
plt.plot(mean0[0],mean0[1],'bo')
plt.plot(mean1[0],mean1[1],'bo')

# covariance of both classes
cov0 = np.cov(x0,y0)
cov1 = np.cov(x1,y1)

# compute the fisher discriminant and plot it (graph of it)
y = perceptron(allxy,allClass)
plt.plot( (0,y[0]) , (0,y[1]) , color="cyan")

# configureation of the plot, save the plot and show it
plt.xlim(-250,250)
plt.ylim(0,180)
plt.savefig("LCA.png")
plt.show()

