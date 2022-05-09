from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)

import xgboost

model = xgboost.XGBRegressor(objective ='reg:linear', n_estimators = 100)
model.fit(X, y)

print(model.predict(X))
