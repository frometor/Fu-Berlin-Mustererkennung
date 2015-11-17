import numpy as np
import math as math
import scipy.stats as scs
mean01=[5,10]
cov01=[[1,1],[1,1]]
import matplotlib.pyplot as plt
x01, y01 = np.random.multivariate_normal(mean01, cov01, 100).T


mean02=[5,5]
cov02=[[2,-1],[-1,2]]
x02, y02 = np.random.multivariate_normal(mean02, cov02, 100).T

mean03=[10,6]
cov03=[[0.1,0],[0,3]]
x03, y03 = np.random.multivariate_normal(mean03, cov03, 100).T


plt.plot(x01, y01, 'x')
plt.plot(x02, y02,'g^')
plt.plot(x03, y03,'bs')

plt.axis('equal')

plt.show()

trueCov01 = np.cov(x01,y01)
pearson01 = scs.pearsonr(x01,y01)

trueCov02 = np.cov(x02,y02)
pearson02 = scs.pearsonr(x02,y02)

trueCov03 = np.cov(x03,y03)
pearson03 = scs.pearsonr(x03,y03)


print('TrueCov01\n',trueCov01)
print('Pearson01\n', pearson01)
print('\n')

print('TrueCov02\n',trueCov02)
print('Pearson02\n', pearson02)
print('\n')

print('TrueCov03\n',trueCov03)
print('Pearson03\n', pearson03)
print('\n')

array01=np.random.randint(-100,100,size=(100,2))
array02=[]
for i in range (0, len(array01)):
    x=np.sqrt(array01[i,0]**2+array01[i,1]**2)
    array02.append(x) 
array03=[]
for j in range (0, len(array01)):
    x=array01[j,0]/(array02[j])
    y=array01[j,1]/(array02[j])
    array03.append([x,y])
   
print(array03)