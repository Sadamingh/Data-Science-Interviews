X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

from sklearn.feature_selection import VarianceThreshold

vt = VarianceThreshold(threshold=.2)
vt.fit(X)
X = vt.transform(X)

print(X)
