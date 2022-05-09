import numpy as np
X = np.random.rand(20, 1000)

print(X.shape)

from sklearn.decomposition import PCA

pca = PCA(n_components=5)
pca.fit(X)
X = pca.transform(X)

print(X.shape)
