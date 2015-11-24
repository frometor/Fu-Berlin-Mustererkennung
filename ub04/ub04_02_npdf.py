# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:00:34 2015

@author: florian
"""
import numpy as np
import matplotlib.pyplot as plt
import gc
import scipy.stats as stats

csv = np.genfromtxt('mouse.csv',delimiter=",")
cluster = np.array([(7,4),(8,6),(9,4)])
colors = ['red','black','blue']
initialCovlist = [([],[]),([],[]),([],[])]    
covMatrixList = [np.identity(2),np.identity(2),np.identity(2)]    
sigmaList = [[],[],[]]


# finds the new centers for the cluster
def find_classes(csv,cluster,subplt,covMatrixList,meanList):    
    newclusterlist = [([],[]),([],[]),([],[])]    
    print(covMatrixList)
    print(np.matrix(covMatrixList[0]))
    for i in range(100):
     # draw the point
        subplt.scatter(csv[i][0],csv[i][1],c=colors[int(csv[i][2])])
        # calculate new class for the point
        safedist = 10000        
        klasse   = 0        
        counter  = 0
        for c in range(len(cluster)):
            print(np.matrix(covMatrixList[c]))                        
            if (safedist > stats.multivariate_normal.pdf(csv[i][0],meanList[c],np.matrix(covMatrixList[c]))):
                safedist = stats.multivariate_normal.pdf(csv[i][0],meanList[c],np.marix(covMatrixList[c]))
                klasse = counter                            
            counter += 1
        csv[i][2] = klasse
        del safedist,klasse,counter
        newclusterlist[int(csv[i][2])][0].append(csv[i][0])
        newclusterlist[int(csv[i][2])][1].append(csv[i][1])
    # draw clustercenters
    for c in cluster:
        subplt.scatter(c[0],c[1] ,c='cyan')    
    covMatrixList = [[],[],[]]      
    # calculate new clustercenters
    for i in range(3):
        cluster[i] = (sum(newclusterlist[i][0])/len(newclusterlist[i][0]),sum(newclusterlist[i][1])/len(newclusterlist[i][1]))        
        covMatrixList[i] = np.cov(newclusterlist[i][0],newclusterlist[i][1]) 
    del newclusterlist
    return csv,cluster


        
# main skript
iteration = 12

# decrement the given classes, to use them as indicies 
# also initial calculation of the covariance-matrix and sigma
for i in range(len(csv)):
    csv[i][2] -= 1
    initialCovlist[int(csv[i][2])][0].append(csv[i][0])
    initialCovlist[int(csv[i][2])][1].append(csv[i][1])

for x in range(3):
    sigmaList[x] = np.mean([initialCovlist[x][0],initialCovlist[x][1]])    

print(np.cov(covMatrixList[0]))    
        
counter = 0
for i in range(iteration):
    counter +=1    
    ax = plt.subplot2grid((3,4), (i/4,i%4))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    # calculate new cluster    
    csv, cluster = find_classes(csv,cluster,ax,covMatrixList,sigmaList)
    gc.collect()
    if (counter%4 == 0):    
        plt.show()
    
plt.show()