from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)

from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor(n_estimators=100)
gbr.fit(X, y)

print(gbr.predict(X))
