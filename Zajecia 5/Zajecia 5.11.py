import numpy as np

mat=np.arange(12)
mat=mat.reshape(3,4)
m1=mat.reshape(4,3)
m2=mat.reshape(2,6)
a=m1.ravel()
print(a)
print(a.shape)
b=m2.ravel()
print(b)
print(b.shape)
