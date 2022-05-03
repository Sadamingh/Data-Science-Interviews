import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, 2, 3, 'a'], [4, 5, 6, 'b'], [7, 8, 9, 'c']]),
                  columns=['a', 'b', 'c', 'index'])

ans = df.set_index('index')

print(ans)
