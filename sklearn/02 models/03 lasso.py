from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)

from sklearn.linear_model import Lasso

lasso = Lasso(alpha=1.0)
lasso.fit(X, y)

print(lasso.predict(X))
