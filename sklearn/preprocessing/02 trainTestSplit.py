import numpy as np
from sklearn.model_selection import train_test_split

X = np.array([[ 1., -1.,  2.],
              [ 2.,  0.,  0.],
              [ 0.,  -1., 0.],
              [ 1.,  1., -1.],
              [ 0.,  2., -2.]])

y = np.array([1, 2, 3, 4, 5])


X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=.2)

print(X_train, y_train, X_test, y_test)
