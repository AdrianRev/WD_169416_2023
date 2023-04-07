import numpy as np

mat=np.arange(9)
mat=mat.reshape(3,3)

for i in range(mat.shape[0]):
    print(mat[i,:])