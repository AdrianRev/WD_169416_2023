import numpy as np

def f(a):
    wektor = np.arange(1, a+1)
    wektor = wektor[::-1]
    m = np.diag(wektor)
    return m


print(f(5))