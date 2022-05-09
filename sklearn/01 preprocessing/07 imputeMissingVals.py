import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

X = pd.DataFrame([[np.nan, 2], [6, np.nan], [7, 6]])

si = SimpleImputer().fit(X)
X = si.transform(X)

print(X)
