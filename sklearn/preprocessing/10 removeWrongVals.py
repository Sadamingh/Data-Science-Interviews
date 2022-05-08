import numpy as np
import pandas as pd

X = pd.DataFrame({"age": [-1, 6, 17, -10], "id": [1, 2, 3, 4]})
print(X)

X = X[X.age < 0]
print(X)
