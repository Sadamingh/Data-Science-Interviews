import numpy as np
X = np.random.rand(20, 1000)

print(X.shape)

from sklearn.decomposition import NMF

nmf = NMF(n_components=5, init='random')
nmf.fit(X)
X = nmf.transform(X)

print(X.shape)
