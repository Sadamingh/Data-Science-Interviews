from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)

from sklearn.linear_model import LinearRegression

ols = LinearRegression()
ols.fit(X, y)

print(ols.predict(X))
