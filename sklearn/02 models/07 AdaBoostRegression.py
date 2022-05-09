from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)

from sklearn.ensemble import AdaBoostRegressor

adaboost = AdaBoostRegressor(n_estimators=100)
adaboost.fit(X, y)

print(adaboost.predict(X))
