import numpy as np

x = np.array([[0, 3, 4],
              [1, 6, 4]])

def normalize_rows(x):
    x_mode = np.linalg.norm(x, axis=1, keepdims=True)
    x = x / x_mode
    return x

print(normalize_rows(x))
