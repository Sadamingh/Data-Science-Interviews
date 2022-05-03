import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, 2, 3, 'a'], [4, 5, 6, 'c'], [7, 8, 9, 'b']]),
                  columns=['a', 'b', 'c', 'index'])

df = df.set_index('index')

ans = df.sort_index()

print(ans)
