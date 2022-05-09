from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(X)

sc = SpectralClustering(n_clusters=3)
sc.fit(X)

print(sc.labels_)
