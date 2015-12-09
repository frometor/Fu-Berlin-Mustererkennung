# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:48:38 2015

@author: erik
"""
import matplotlib.pyplot as plt
import numpy as np

    
def schnittpunktGauss(mean0,mean1,sigma0,sigma1):
    p = (2*(mean1*sigma0**2 - mean0*sigma1**2) / (sigma0**2 - sigma1**2))
    q = (mean0**2 * sigma1**2 - mean1**2 * sigma0**2 - 2*np.log(sigma1/sigma0) * sigma0**2 * sigma1**2) / (sigma1**2 - sigma0**2 )  
    x1 = -p/2 + np.sqrt((p/2)**2 - q) 
    x2 = -p/2 - np.sqrt((p/2)**2 - q)
    return x1,x2


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
skalar = 1
y = skalar * np.dot((np.linalg.inv(cov0+cov1)), (mean0-mean1))
plt.plot( (-y[0]*2000,y[0]*2000) , (-y[1]*2000,y[1]*2000) , color="cyan")

# compute new mean
newMean0 = np.dot(mean0,y)
newMean1 = np.dot(mean1,y)

# compute sigma for projected data
sigma0 = np.dot(np.dot(y.T,cov0),y)
sigma1 = np.dot(np.dot(y.T,cov1),y)

# compute the intersection of both n-pdf
x1,x2 = schnittpunktGauss(newMean0,newMean1,sigma0,sigma1)
print "Schnittpunkt1 :",x1
print "Schnittpunkt2 :",x2

# projekt the intersection-points onto the line
projektX1 = np.dot(np.dot(x1,y),x1)
projektX2 = np.dot(np.dot(x2,y),x2)

print "Schnittpunkt1 projeziert:",projektX1
print "Schnittpunkt2 projeziert:",projektX2

plt.plot(projektX1[0],projektX1[1],'bo')
plt.plot(projektX2[0],projektX2[1],'bo')


# configureation of the plot, save the plot and show it
plt.xlim(-250,250)
plt.ylim(-50,180)
plt.savefig("LCA.png")
plt.show()

