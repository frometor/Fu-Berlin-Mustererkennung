# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:00:34 2015

@author: florian
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

csv = np.genfromtxt('mouse.csv',delimiter=",")
cluster = np.array([(7,4),(8,6),(9,4)])
colors = ['red','black','blue']
initialCovlist = [([],[]),([],[]),([],[])]    
covMatrixList = [np.identity(2),np.identity(2),np.identity(2)]    
meanList = [(),(),()]

# finds the new centers for the cluster
def find_classes(csv,cluster,covMatrixList,meanList,subplt):    
    newclusterlist = [([],[]),([],[]),([],[])]    
    newMeanList = [(),(),()]
    for i in range(len(csv)):
        # draw the point
        subplt.scatter(csv[i][0],csv[i][1],c=colors[int(csv[i][2])])
        # calculate new class for the point
        safedist = 10000        
        klasse   = 0        
        counter  = 0
        for c in range(len(cluster)):
            x = [float(csv[i][0]),float(csv[i][1])]
            if (safedist > stats.multivariate_normal.pdf(x,meanList[c],np.matrix(covMatrixList[c]))):
                safedist = stats.multivariate_normal.pdf(x,meanList[c],np.matrix(covMatrixList[c]))
                klasse = counter                            
            counter += 1
        csv[i][2] = klasse
        newclusterlist[int(csv[i][2])][0].append(csv[i][0])
        newclusterlist[int(csv[i][2])][1].append(csv[i][1])
    # draw clustercenters
    for c in cluster:
        subplt.scatter(c[0],c[1] ,c='cyan')    
    # calculate new clustercenter and new covariance matrix
    newCovMatrixList = [[],[],[]]              
    for i in range(3):
        if(len(newclusterlist[i][0]) != 0):
            cluster[i] = (sum(newclusterlist[i][0])/len(newclusterlist[i][0]),sum(newclusterlist[i][1])/len(newclusterlist[i][1]))        
            newCovMatrixList[i] = np.cov(newclusterlist[i][0],newclusterlist[i][1])
            newMeanList[i] = (np.mean(newCovMatrixList[i][0]), np.mean(newCovMatrixList[i][1]))
        else:
            newCovMatrixList[i] = covMatrixList[i]
            newMeanList[i] = meanList[i]
    del newclusterlist
    return csv,cluster,newCovMatrixList,newMeanList


        
# main skript
iteration = 12

# decrement the given classes, to use them as indicies 
for i in range(len(csv)):
    csv[i][2] -= 1
    initialCovlist[int(csv[i][2])][0].append(csv[i][0])
    initialCovlist[int(csv[i][2])][1].append(csv[i][1])

# initial calculation of the covariance-matrix and sigma
for x in range(3):    
    meanList[x] = (np.mean(initialCovlist[x][0]), np.mean(initialCovlist[x][1]))

       
counter = 0
for i in range(iteration):
    counter +=1    
    ax = plt.subplot2grid((3,4), (i/4,i%4))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    # calculate new cluster    
    csv, cluster,covMatrixList, meanList = find_classes(csv,cluster,covMatrixList,meanList,ax)
    print(covMatrixList[0])
    print(covMatrixList[1])
    print(covMatrixList[2])
    if (counter%4 == 0):    
        plt.show()
    
plt.show()