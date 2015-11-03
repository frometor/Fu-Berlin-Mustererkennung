import numpy as np
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_mldata
from sklearn import cluster, datasets
customhome = '~/Documents/Mustererkennung/ub01'

mnist = fetch_mldata('MNIST original', data_home= customhome)
mnist.data, mnist.target = shuffle(mnist.data, mnist.target)

# We reduce the dataset size, otherwise it'll take too much time to run
mnist.data = mnist.data[:10000]
mnist.target = mnist.target[:10000]

X_train, X_test, y_train, y_test = train_test_split(mnist.data, mnist.
target, test_size=0.1, random_state=0)
k_means = cluster.KMeans(n_clusters=9)
k_means.fit(mnist.data)
print (k_means.labels_[::10])
print (mnist.target[::10])
#N_samples = 2000
#dataset_1 = np.array(datasets.make_circles(n_samples=N_samples,
#noise=0.05, factor=0.3)[0])

#dataset_2 = np.array(datasets.make_blobs(n_samples=N_samples, centers=4,
#cluster_std=0.4, random_state=0)[0])

#plt.scatter(dataset_1[:,0], dataset_1[:,1], c='k', alpha=0.8, s=5.0)
#plt.scatter(dataset_2[:,0], dataset_2[:,1], c='k', alpha=0.8, s=5.0)
#plt.show()