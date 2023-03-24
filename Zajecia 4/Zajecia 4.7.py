import numpy as np

def f(n):
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i==j:
                m[i][j]=2
            elif i<j:
                m[i][j]=2+(2*(j-i))
            else:
                m[i][j]=2+(2*(i-j))
    return m
print(f(4))