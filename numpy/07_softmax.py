import numpy as np

t_x = np.array([[9, 2, 5, 0, 0],
                [7, 5, 0, 0 ,0]])

# GRADED FUNCTION: softmax

def softmax(x):
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    s = x_exp / x_sum
    return s

print(softmax(t_x))
