import math

def basic_sigmoid(x):
    s = 1 / (1 + math.exp(-x))
    return s

print(basic_sigmoid(5))
