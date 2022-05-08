import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

X = pd.DataFrame([[0, 2], [6, 0], [7, 6], [4, 5]])

si = SimpleImputer(missing_values=0, strategy='median')
si.fit(X)
X = si.transform(X)

print(X)
