import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import scipy.stats as stats
import math

#functions
#gets row(of chicken_csv) and a list of (means,sigmas) 
#and returns the best class for that row
def returnClass(row,list):
    safewkt=0
    safeclass = 0
    for x in range(0,6):
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

x = np.linspace(0,500,5000)

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
print('Varianz 0: ',np.var(array0np[:,1]))
print('A-Priori 0:',(float(cnt0)/len(csv)))
mean= np.mean(array0np[:,1])
sigma= math.sqrt(np.var(array0np[:,1]))
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='red')
red_patch = mpatches.Patch(color='red', label='class1')

print('class1 = blue')
print('Erwartungswert 1: ',np.mean(array1np[:,1]))
print('Varianz 1: ',np.var(array1np[:,1]))
print('A-Priori 0:',(float(cnt1)/len(csv)))
mean= np.mean(array1np[:,1])
sigma= math.sqrt(np.var(array1np[:,1]))
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='b')
blue_patch = mpatches.Patch(color='blue', label='class2')

print('class2 = green')
print('Erwartungswert 2: ',np.mean(array2np[:,1]))
print('Varianz 2: ',np.var(array2np[:,1]))
print('A-Priori 0:',(float(cnt2)/len(csv)))
mean= np.mean(array2np[:,1])
sigma= math.sqrt(np.var(array2np[:,1]))
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='green')
green_patch = mpatches.Patch(color='green', label='class3')

print('class3 = black')
print('Erwartungswert 3: ',np.mean(array3np[:,1]))
print('Varianz 3: ',np.var(array3np[:,1]))
print('A-Priori 0:',(float(cnt3)/len(csv)))
mean= np.mean(array3np[:,1])
sigma= math.sqrt(np.var(array3np[:,1]))
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='black')
black_patch = mpatches.Patch(color='black', label='class4')

print('class4 = yellow')
print('Erwartungswert 4: ',np.mean(array4np[:,1]))
print('Varianz 4: ',np.var(array4np[:,1]))
print('A-Priori 0:',(float(cnt4)/len(csv)))
mean= np.mean(array4np[:,1])
sigma= math.sqrt(np.var(array4np[:,1]))
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='yellow')
yellow_patch = mpatches.Patch(color='yellow', label='class5')

print('class5 = orange')
print('Erwartungswert 5:',np.mean(array5np[:,1]))
print('Varianz 5: ',np.var(array5np[:,1]))
print('A-Priori 0:',(float(cnt5)/len(csv)))
mean= np.mean(array5np[:,1])
sigma= math.sqrt(np.var(array5np[:,1]))
meanAndSigma.append((mean,sigma))
plt.plot(x,stats.norm.pdf(x,mean,sigma),c='orange')
orange_patch = mpatches.Patch(color='orange', label='class6')


plt.legend(bbox_to_anchor=(1,1),loc=2,handles=[red_patch,blue_patch,green_patch,black_patch,yellow_patch,orange_patch])
plt.show()



# exercise 1c)
csv = np.genfromtxt('chickwts_testing.csv', delimiter=",")
confusionMatrix = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

classifikationquality = 0.0
counterall = 0.0
for row in csv:
    counterall += 1    
    predicted_class = returnClass(row,meanAndSigma)
    confusionMatrix[int(row[2])][predicted_class] += 1
    if (int(row[2]) == predicted_class):
        classifikationquality += 1

        
print('\n\n')
print('confusionmatrix:')
for row in confusionMatrix:
    print(row)

print('classifikationqualtiy: '+ str(classifikationquality/counterall))       
    