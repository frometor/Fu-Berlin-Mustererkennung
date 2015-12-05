# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:02:42 2015

@author: florian and erik
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import matplotlib.patches as mpatches

def s(ux_mean,uy_mean,ux,uy):
    sSpeicher = 0
    xSpeicher = 0    
    for x in range(len(ux_mean)):
        absMean = np.abs(ux_mean[x]-uy_mean[x])
        varSum = ux[x]+uy[x]
        s = absMean / varSum
        if(s > sSpeicher):
            sSpeicher = s
            xSpeicher = x
    return xSpeicher


#2_a)
mean1=[5,10]
covarianzmatrix1= [[1, 1], [1, 1]]

mean2=[5,5]
covarianzmatrix2=[[2,-1],[-1,2]]

mean3=[10,6]
covarianzmatrix3=[[0.1,0],[0,3]]


x1,y1 = np.random.multivariate_normal(mean1,covarianzmatrix1,100).T
x2,y2 = np.random.multivariate_normal(mean2,covarianzmatrix2,100).T
x3,y3 = np.random.multivariate_normal(mean3,covarianzmatrix3,100).T

plt.plot(x1,y1,'x',c='red')
plt.plot(x2,y2,'x',c='blue')
plt.plot(x3,y3,'x',c='green')

plt.show()
plt.plot(x1,y1,'x',c='red')
plt.plot(x2,y2,'x',c='blue')
plt.plot(x3,y3,'x',c='green')

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

#2_c)
u1_mean,u2_mean,u3_mean,u1,u2,u3 = [],[],[],[],[],[]

array01=np.random.randint(-100,100,size=(1000,2))
array02=[]
for i in range (0, len(array01)):
    x=np.sqrt(array01[i,0]**2+array01[i,1]**2)
    array02.append(x) 
array03=[]
for j in range (0, len(array01)):
    x=array01[j,0]/(array02[j])
    y=array01[j,1]/(array02[j])
    array03.append([x,y])  
array03np = np.array(array03)    
    
for xyTupel in array03np:
    u1_mean.append(np.dot(mean1,xyTupel))
    u2_mean.append(np.dot(mean2,xyTupel))
    u3_mean.append(np.dot(mean3,xyTupel))
    u1.append((np.dot(np.dot(xyTupel.T,new_covarianzmatrix1),xyTupel)))
    u2.append((np.dot(np.dot(xyTupel.T,new_covarianzmatrix2),xyTupel)))
    u3.append((np.dot(np.dot(xyTupel.T,new_covarianzmatrix3),xyTupel)))




ax = plt.subplot()
plt.plot([(array03[s(u1_mean,u2_mean,u1,u2)][0]*-20),(array03[s(u1_mean,u2_mean,u1,u2)][0])*20],[(array03[s(u1_mean,u2_mean,u1,u2)][1])*-20,(array03[s(u1_mean,u2_mean,u1,u2)][1])*20],c='#800080')
plt.plot([(array03[s(u1_mean,u3_mean,u1,u3)][0]*-20),(array03[s(u1_mean,u3_mean,u1,u3)][0])*20],[(array03[s(u1_mean,u3_mean,u1,u3)][1])*-20,(array03[s(u1_mean,u3_mean,u1,u3)][1])*20],c='#998000')
plt.plot([(array03[s(u2_mean,u3_mean,u2,u3)][0]*-20),(array03[s(u2_mean,u3_mean,u2,u3)][0])*20],[(array03[s(u2_mean,u3_mean,u2,u3)][1])*-20,(array03[s(u2_mean,u3_mean,u2,u3)][1])*20],c='#008080')


#plot set up
red_patch = mpatches.Patch(color='red', label='class1')
blue_patch = mpatches.Patch(color='blue', label='class2')
black_patch = mpatches.Patch(color='green', label='class3')
first_line_patch = mpatches.Patch(color='#800080', label='line for class 1 and 2')
nd_line_patch = mpatches.Patch(color='#998000', label='line for class 1 and 3')
rd_line_red_patch = mpatches.Patch(color='#008080', label='line for class 2 and 3')
plt.legend(bbox_to_anchor=(1,1),loc=2,handles=[red_patch,blue_patch,black_patch,first_line_patch,nd_line_patch,rd_line_red_patch])

ax.set_xlim([-10,15])
ax.set_ylim([-10,15])

plt.show()







    