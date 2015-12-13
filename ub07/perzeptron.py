# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:48:38 2015

@author: erik
"""
import matplotlib.pyplot as plt
import numpy as np

# perceptron-algorithem with x corrections
def percepton(xyClass,belongingClass):
    k = 0    
    x = 3000
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
# b)
#        y = w + x
#        y_orth = perpendicular(y)
#        plt.plot((-100000*y[0],y[0]*100000),(-100000*y[1],y[1]*100000),color='yellow')
#        plt.plot((-100000*y_orth[0],y_orth[0]*100000),(-100000*y_orth[1],y_orth[1]*100000),color='green')
        return w + x ,k+1

def perceptonNegativ(w,x,k):        
    if (w.dot < 0):
        return w,k
    else:        
# b)
#        y = w + x
#        y_orth = perpendicular(y)
#        plt.plot((-100000*y[0],y[0]*100000),(-100000*y[1],y[1]*100000),color='yellow')
#        plt.plot((-100000*y_orth[0],y_orth[0]*100000),(-100000*y_orth[1],y_orth[1]*100000),color='green')
        return w - x, k+1
       

# computes a orthogonal vector
def perpendicular( a ) :    
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b
    
def myMean(list):
    a0 = 0
    a1 = 0
    for x in list:
        a0 += x[0]
        a1 += x[1]
        return [a0/len(list),a1/len(list)]
#----------------------------- main -----------------------------
    
# loadData
csv = np.genfromtxt('klausur.txt',delimiter=";")
allClass0,allClass1 = [],[]
allgreats,allClass = [],[]
x0_P,y0_P,x1_P,y1_P = [],[],[],[]
yList = []

for row in csv:
    if (row[1]):
        allClass1.append(row[0])
    else:
        allClass0.append(row[0])
    allgreats.append((row[0],1))
    allClass.append(row[1])


# compute perzepton line
# b)
#y = percepton(allgreats,allClass)
#y_orth = perpendicular(y)
# c)
for x in range(100):
    y = percepton(allgreats,allClass)
    y_orth = perpendicular(y)
    yList.append(y)
yMean = myMean(yList)
print(yMean)
yMean_orth = perpendicular(yMean)


    
# plot all point | first plot looks better than the new one
for x in range(len(allgreats)):
    if (allClass[x] == 0):
        plt.scatter(allgreats[x][0],allgreats[x][1],color="red")
    else:
        plt.scatter(allgreats[x][0],allgreats[x][1],color="yellow")
# plot the main lines 
# b)
#plt.plot((-100000*y[0],y[0]*100000),(-100000*y[1],y[1]*100000),color='black')
#plt.plot((-100000*y_orth[0],y_orth[0]*100000),(-100000*y_orth[1],y_orth[1]*100000),color='black')
# c)
plt.plot((-100000*yMean[0],yMean[0]*100000),(-100000*yMean[1],yMean[1]*100000),color='black')
plt.plot((-100000*yMean_orth[0],yMean_orth[0]*100000),(-100000*yMean_orth[1],yMean_orth[1]*100000),color='black')



plt.xlim(-0.5,1.1)
plt.ylim(-0.5,1.5)
plt.savefig("klausur_plot.png")
plt.show()

