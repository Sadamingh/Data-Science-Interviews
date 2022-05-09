import numpy as np
X = np.random.rand(20, 10)
y = np.random.rand(20)

print(X.shape, y.shape)

from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LinearRegression

ols = LinearRegression()
sfs = SequentialFeatureSelector(ols, n_features_to_select=5, direction='forward')
sfs.fit(X, y)
X = sfs.transform(X)

print(X.shape, y.shape)
