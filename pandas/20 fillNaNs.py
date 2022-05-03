import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, np.NaN, 3], [4, 5, 6], [7, 8, np.NaN]]),
                  columns=['a', 'b', 'c'])

ans = df.fillna(0)

print(ans)
