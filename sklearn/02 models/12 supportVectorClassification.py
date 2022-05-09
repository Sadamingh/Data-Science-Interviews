from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(X)
svc = SVC()
svc.fit(X, y)

print(svc.predict(X))
