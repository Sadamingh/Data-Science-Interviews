from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)

from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(X, y)

print(ridge.predict(X))
