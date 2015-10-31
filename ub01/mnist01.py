#%matplotlib inline
import random
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
import matplotlib.cm as cm
customhome = '~/Documents/Mustererkennung/ub01'

mnist_dt = fetch_mldata('MNIST original', data_home= customhome).data
mnist_tg = fetch_mldata('MNIST original', data_home= customhome).target

print('data.shape: ', mnist_dt.shape)
print('target.shape: ',mnist_tg.shape)

cnt = 1
for i in range (1, 3):
    for j in range (1, 6):
        plt.subplot(2,5, cnt)
        rand =random.randint(1,70000)
        print (mnist_tg[rand])
        plt.imshow(mnist_dt[rand].reshape((28, 28)),cmap=cm.Greys_r)
        plt.axis('off')
        cnt+=1
plt.show()