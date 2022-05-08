import pandas as pd
import numpy as np
from sklearn.preprocessing import OrdinalEncoder

df = pd.DataFrame()
df['gender'] = pd.Series(['male', 'female', 'prefer not to say'])
gender = np.array(df.gender).reshape(-1, 1)

oe = OrdinalEncoder().fit(gender)
df.gender = oe.transform(gender)

print(df)
