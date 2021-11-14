import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None,nR=30,nC=30):
        number_columns, number_rows = X.shape[0], X.shape[1]
        return [[X[int(number_rows * r / nR)][int(number_columns * c / nC)]for c in range(nC)] for r in range(nR)]
X=np.random.random((50,50))
c=imshow(X)
print(np.shape(c))
