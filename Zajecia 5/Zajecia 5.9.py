import numpy as np

mat=np.arange(9).reshape(3,3)
print(mat)
for i in mat.flat:
    print(i)

