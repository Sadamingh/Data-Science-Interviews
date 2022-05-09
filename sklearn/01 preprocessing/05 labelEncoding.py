import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

y = pd.Series(['male', 'female', 'prefer not to say'])

ohe = LabelEncoder().fit(y)
print(ohe.transform(y))
