import numpy as np
X = np.random.rand(20, 1000)

print(X.shape)

from sklearn.decomposition import LatentDirichletAllocation

lda = LatentDirichletAllocation(n_components=5)
lda.fit(X)
X = lda.transform(X)

print(X.shape)
