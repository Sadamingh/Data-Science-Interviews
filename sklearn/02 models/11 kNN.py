from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(X)
kNN = KNeighborsClassifier(n_neighbors=3)
kNN.fit(X, y)

print(kNN.predict(X))
