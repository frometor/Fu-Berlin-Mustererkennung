import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

#functions
#gets row(of chicken_csv) and a list of (means,sigmas) 
#and returns the best class for that row
def returnClass(row,list):
    counter = 0    
    safewkt=0
    safeclass = 0
    for x in range(0,5):
        counter += 1
        wkt = stats.norm.pdf(row[1],meanAndSigma[x][0],meanAndSigma[x][1])
        if (safewkt < wkt):
            safewkt = wkt
            safeclass = x
    return safeclass
 


#exercise 1a and b)
csv = np.genfromtxt('chickwts_training.csv', delimiter=",")
array0= []
array1= []
array2= []
array3= []
array4= []
array5= []

i=0
cnt0=0
cnt1=0
cnt2=0
cnt3=0
cnt4=0
cnt5=0

x = np.linspace(100,400,5000)

for i in range(len(csv)):
    if (csv[i][2] == 0):
        array0.append(csv[i])
        cnt0+=1
    elif (csv[i][2] == 1):
        array1.append(csv[i])
        cnt1+=1
    elif (csv[i][2] == 2):
        array2.append(csv[i])
        cnt2+=1
    elif (csv[i][2] == 3):
        array3.append(csv[i])
        cnt3+=1
    elif (csv[i][2] == 4):
        array4.append(csv[i])
        cnt4+=1
    elif (csv[i][2] == 5):
        array5.append(csv[i])
        cnt5+=1

array0np=np.array(array0)
array1np=np.array(array1)
array2np=np.array(array2)
array3np=np.array(array3)
array4np=np.array(array4)
array5np=np.array(array5)

meanAndSigma = []

print('class0 = red')
print('Erwartungswert 0: ',np.mean(array0np[:,1]))
print('Standartabweichung 0: ',np.std(array0np[:,1]))
print('A-Priori 0:',(float(cnt0)/len(csv)))
mean= np.mean(array0np[:,1])
sigma= math.sqrt(mean)
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='red')

print('class1 = blue')
print('Erwartungswert 1: ',np.mean(array1np[:,1]))
print('Standartabweichung 1: ',np.std(array1np[:,1]))
print('A-Priori 0:',(float(cnt1)/len(csv)))
mean= np.mean(array1np[:,1])
sigma= math.sqrt(mean)
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='b')

print('class2 = green')
print('Erwartungswert 2: ',np.mean(array2np[:,1]))
print('Standartabweichung 2: ',np.std(array2np[:,1]))
print('A-Priori 0:',(float(cnt2)/len(csv)))
mean= np.mean(array2np[:,1])
sigma= math.sqrt(mean)
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='green')

print('class3 = black')
print('Erwartungswert 3: ',np.mean(array3np[:,1]))
print('Standartabweichung 3: ',np.std(array3np[:,1]))
print('A-Priori 0:',(float(cnt3)/len(csv)))
mean= np.mean(array3np[:,1])
sigma= math.sqrt(mean)
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='black')

print('class4 = yellow')
print('Erwartungswert 4: ',np.mean(array4np[:,1]))
print('Standartabweichung 4: ',np.std(array4np[:,1]))
print('A-Priori 0:',(float(cnt4)/len(csv)))
mean= np.mean(array4np[:,1])
sigma= math.sqrt(mean)
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='yellow')

print('class5 = orange')
print('Erwartungswert 5:',np.mean(array5np[:,1]))
print('Standartabweichung 5: ',np.std(array5np[:,1]))
print('A-Priori 0:',(float(cnt5)/len(csv)))
mean= np.mean(array5np[:,1])
sigma= math.sqrt(mean)
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='orange')

plt.show()



# exercise 1c)
csv = np.genfromtxt('chickwts_testing.csv', delimiter=",")
confusionMatrix = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]


for row in csv:
    predicted_class = returnClass(row,meanAndSigma)
    confusionMatrix[predicted_class][int(row[2])] += 1

print('\n\n')
print('confusionmatrix:')
for row in confusionMatrix:
    print(row)
    