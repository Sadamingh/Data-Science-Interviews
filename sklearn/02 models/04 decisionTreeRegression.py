from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)

from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(max_features=.6, max_depth=20, min_samples_leaf=5)
dt.fit(X, y)

print(dt.predict(X))
