import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

X = pd.DataFrame({"val": [0, 6, 7, 4]})

print(X)

si = SimpleImputer(missing_values=0, strategy='median')
si.fit(np.array(X.val).reshape(-1, 1))
X.val = si.transform(np.array(X.val).reshape(-1, 1))

print(X)
