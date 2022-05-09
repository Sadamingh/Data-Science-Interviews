from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

X = StandardScaler().fit_transform(X)

logit = LogisticRegression()
logit.fit(X, y)

print(logit.predict_proba(X))
print(logit.predict(X))
