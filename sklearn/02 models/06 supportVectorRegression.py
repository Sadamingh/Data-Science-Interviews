from sklearn.datasets import load_diabetes
X, y = load_diabetes(return_X_y=True)

from sklearn.svm import SVR

svr = SVR(C=1.0, epsilon=0.1)
svr.fit(X, y)

print(svr.predict(X))
