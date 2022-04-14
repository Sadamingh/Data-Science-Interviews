# Summerize a matrix by its rows
import numpy as np

x = np.array([[0, 3, 4],
              [1, 6, 4]])

def sum_rows(x):
    x = np.sum(x, axis=1, keepdims=True)
    return x

print(sum_rows(x))
