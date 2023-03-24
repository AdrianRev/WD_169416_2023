import numpy as np

def fib(n):
    if n == 1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
mat=np.arange(25)
for i in range(1,25):
    mat[i]=fib(i)

mat=mat.reshape(5,5)
print(mat)
