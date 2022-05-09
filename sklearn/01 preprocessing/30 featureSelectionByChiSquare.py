X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
y = [1, 0, 1, 0, 0, 1]

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

kbest = SelectKBest(chi2, k=2)
kbest.fit(X, y)
X = kbest.transform(X)

print(X)
