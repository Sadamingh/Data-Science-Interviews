from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

from sklearn.ensemble import AdaBoostClassifier

adaboost = AdaBoostClassifier(n_estimators=100)
adaboost.fit(X, y)

print(adaboost.predict(X))
