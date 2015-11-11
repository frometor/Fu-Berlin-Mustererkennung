import numpy as np
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

print(array0np.shape)
print('Erwartungswert 0: ',np.mean(array0np[:,1]))
print('Standartabweichung 0: ',np.std(array0np[:,1]))

print('Erwartungswert 1: ',np.mean(array1np[:,1]))
print('Standartabweichung 1: ',np.std(array1np[:,1]))

print('Erwartungswert 2: ',np.mean(array2np[:,1]))
print('Standartabweichung 2: ',np.std(array2np[:,1]))

print('Erwartungswert 3: ',np.mean(array3np[:,1]))
print('Standartabweichung 3: ',np.std(array3np[:,1]))

print('Erwartungswert 4: ',np.mean(array4np[:,1]))
print('Standartabweichung 4: ',np.std(array4np[:,1]))

print('Erwartungswert 5:',np.mean(array5np[:,1]))
print('Standartabweichung 5: ',np.std(array5np[:,1]))


#print(array0np[:,1])
#sliceofArray0 = array0np[:,1]   
    
#print(sliceofArray0)
#print(np.std(csv,axis=0))
#print(csv.shape)