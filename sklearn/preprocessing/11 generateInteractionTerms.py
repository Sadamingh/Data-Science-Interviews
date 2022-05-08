import numpy as np
import pandas as pd

X = pd.DataFrame({"x1": [-1, 6, 17, -10], "x2": [1, 2, 3, 4]})
print(X)

X["x1x2"] =  X.x1 * X.x2
print(X)
