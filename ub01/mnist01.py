import random
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
import matplotlib.cm as cm
customhome = '~/Documents/Mustererkennung/ub01'

mnist = fetch_mldata('MNIST original', data_home= customhome).data
counter = 1
for i in range (1, 3):
    for j in range (1, 6):
        plt.subplot(3,5, counter)
        plt.imshow(mnist[(((random.randint(0,9))) * 7000)].reshape((28, 28)),cmap=cm.Greys_r)
        plt.axis('off')
        counter+=1
plt.show()