from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(max_features=.6, max_depth=20, min_samples_leaf=5)
dt.fit(X, y)

print(dt.predict(X))
