from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(X)

km = KMeans(n_clusters=3, init='k-means++')
km.fit(X)

print(km.predict(X))
