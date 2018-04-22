import numpy as np
from sklearn.decomposition import PCA

l = np.array([[2,3,4,5,6],[4,6,3,7,3],[3,6,2,7,8]])
pca = PCA(n_components=2)
pca.fit(l)
x = pca.transform(l)
print(x)

