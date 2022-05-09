import numpy as np
X = np.random.rand(20, 1000)

print(X.shape)

from sklearn.manifold import TSNE

tSNE = TSNE(n_components=2, learning_rate='auto', init='random')
X = tSNE.fit_transform(X)

print(X.shape)
