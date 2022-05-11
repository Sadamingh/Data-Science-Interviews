import numpy as np
y = np.array([1,2,3,4,5,6,7])
yhat = np.array([1,1,3.5,6,6,6,7])

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y, yhat, squared=False))
