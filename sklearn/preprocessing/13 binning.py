# Good to use for noisy data
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer

X = np.array([[ -3., 5., 15 ],
              [  0., 6., 14 ],
              [  6., 3., 11 ]])

bin = KBinsDiscretizer(n_bins=[3, 2, 2], encode='ordinal')
bin.fit(X)
X = bin.transform(X)

print(X)
