import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, 2, 3], [1, 2, 3], [7, 8, 9]]),
                  columns=['a', 'b', 'c'])

ans = df.drop_duplicates()

print(ans)
