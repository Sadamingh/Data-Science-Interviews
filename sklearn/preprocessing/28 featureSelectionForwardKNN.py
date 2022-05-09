import numpy as np
X = np.random.rand(200, 10)
y = np.random.randint(20, size=(200,))

print(X.shape, y.shape)

from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.neighbors import KNeighborsClassifier

ols = KNeighborsClassifier(n_neighbors=3)
sfs = SequentialFeatureSelector(ols, n_features_to_select=5, direction='forward')
sfs.fit(X, y)
X = sfs.transform(X)

print(X.shape, y.shape)
