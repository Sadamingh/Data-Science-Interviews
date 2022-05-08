import numpy as np
from sklearn.preprocessing import StandardScaler

X = np.array([[ 1., -1.,  2.],
              [ 2.,  0.,  0.],
              [ 0.,  1., -1.]])

scaler = StandardScaler().fit(X)
print(scaler.transform(X))
