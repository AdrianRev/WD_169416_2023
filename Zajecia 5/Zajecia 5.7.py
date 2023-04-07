import numpy as np

mat=np.arange(6)
mat=mat.reshape(2,3)
print(mat)
a=np.sin(mat)
b=np.cos(mat)
print(a+b)