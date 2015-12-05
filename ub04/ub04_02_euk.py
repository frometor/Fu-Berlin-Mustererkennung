# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:22:34 2015

@author: florian
"""
import numpy as np
import matplotlib.pyplot as plt
import gc

csv = np.genfromtxt('mouse.csv',delimiter=",")
cluster = np.array([(7,4),(8,6),(9,4)])
colors = ['red','black','blue']

# euklidische distanz
# dist = numpy.linalg.norm(a-b)
def distance_euk(x,y,c):
    return ((x-c[0])**2 + (y-c[1])**2)    


# finds the new centers for the cluster
def find_classes(csv,cluster,subplt):    
    newclusterlist = [([],[]),([],[]),([],[])]    
    for i in range(len(csv)):
     # draw the point
        subplt.scatter(csv[i][0],csv[i][1],c=colors[int(csv[i][2])])
        # calculate new class for the point
        safedist = 10000        
        klasse   = 0        
        counter  = 0
        for c in cluster:                        
            if (safedist > distance_euk(csv[i][0],csv[i][1],c)):
                safedist = distance_euk(csv[i][0],csv[i][1],c)
                klasse = counter                            
            counter += 1
        csv[i][2] = klasse
        del safedist,klasse,counter
        newclusterlist[int(csv[i][2])][0].append(csv[i][0])
        newclusterlist[int(csv[i][2])][1].append(csv[i][1])
    # draw clustercenters
    for c in cluster:
        subplt.scatter(c[0],c[1] ,c='cyan')    
    # calculate new clustercenters
    for i in range(3):
        cluster[i] = (sum(newclusterlist[i][0])/len(newclusterlist[i][0]),sum(newclusterlist[i][1])/len(newclusterlist[i][1]))        
    del newclusterlist
    return csv,cluster


        
# main skript
iteration = 12

# decrement the given classes, to use them as indicies 
for i in range(len(csv)):
    csv[i][2] -= 1
 
counter = 0
for i in range(iteration):
    counter +=1    
    ax = plt.subplot2grid((3,4), (i/4,i%4))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    # calculate k-means
    csv, cluster = find_classes(csv,cluster,ax)
    gc.collect()
    if (counter%4 == 0):    
        plt.show()
    
plt.show()