import numpy as np
true_cov = np.array([[.5, .6],[.6, .4]])
X = np.random.RandomState(0).multivariate_normal(mean=[0, 0], cov=true_cov,size=500)

from sklearn.neighbors import LocalOutlierFactor
lof = LocalOutlierFactor(novelty=True).fit(X)
isOutlier = lof.predict(X)

import matplotlib.pyplot as plt
for (x, y), c in zip(X, isOutlier):
    if c == -1:
        plt.scatter(x, y, color="r")
    else:
        plt.scatter(x, y, color="b")
plt.title("red = outlier, blue = inlier")
plt.show()
