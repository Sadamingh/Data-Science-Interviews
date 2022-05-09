import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

df = pd.DataFrame()
df['gender'] = pd.Series(['male', 'female', 'prefer not to say'])
gender = np.array(df.gender).reshape(-1, 1)

ohe = OneHotEncoder().fit(gender)
gender_ohe = ohe.transform(gender).toarray()

df = pd.concat([df, pd.DataFrame(gender_ohe)], axis=1).drop(columns=["gender"])

print(df)
