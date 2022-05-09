import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer

X = pd.DataFrame({"val": [0, 6, 7, 4, 0, 1, 9, 0, 2, 3]})

print(X)

si = KNNImputer(missing_values=0, n_neighbors=2, weights="uniform")
si.fit(np.array(X.val).reshape(-1, 1))
X.val = si.transform(np.array(X.val).reshape(-1, 1))

print(X)
