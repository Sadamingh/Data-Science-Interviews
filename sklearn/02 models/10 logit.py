from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.linear_model import LogisticRegression

logit = LogisticRegression()
logit.fit(X, y)

print(logit.predict(X))
