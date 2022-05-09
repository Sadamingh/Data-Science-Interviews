import numpy as np
X = np.random.rand(20, 1000)

print(X.shape)

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD

scaler = StandardScaler().fit(X)
X = scaler.transform(X)

svd = TruncatedSVD(n_components=5)
svd.fit(X)
X = svd.transform(X)

print(X.shape)
