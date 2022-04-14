import numpy as np

def basic_sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s

print(basic_sigmoid(np.array([1,2,3])))
