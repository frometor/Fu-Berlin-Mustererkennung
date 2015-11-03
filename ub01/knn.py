from sklearn.utils import shuffle
from sklearn.datasets import fetch_mldata
from sklearn.cross_validation import train_test_split
              
customhome = '~/Documents/Mustererkennung/ub01'

mnist = fetch_mldata('MNIST original', data_home= customhome)
mnist.data, mnist.target = shuffle(mnist.data, mnist.target)

# We reduce the dataset size, otherwise it'll take too much time to run
mnist.data = mnist.data[:10000]
mnist.target = mnist.target[:10000]

X_train, X_test, y_train, y_test = train_test_split(mnist.data, mnist.
target, test_size=100, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
k = 11
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


print ('k = ',k)
print (classification_report(y_test, y_pred))