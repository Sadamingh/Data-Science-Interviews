from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)

import xgboost

model = xgboost.XGBClassifier(objective ='binary:logistic', n_estimators = 100)
model.fit(X, y)

print(model.predict(X))
