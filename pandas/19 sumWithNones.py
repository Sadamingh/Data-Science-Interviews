import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, None, 3], [4, 5, 6], [7, 8, None]]),
                  columns=['a', 'b', 'c'])

ans = df.sum(axis=1)

print(ans)
