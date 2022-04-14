import numpy as np

def sigmoid_derivative(x):
    s = 1 / (1 + np.exp(-x))
    ds = s * (1 - s)
    return ds

print(sigmoid_derivative(np.array([1,2,3])))
