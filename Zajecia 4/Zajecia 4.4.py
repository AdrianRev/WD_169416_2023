import numpy as np
import math

def potegi(a, n):
    x = np.logspace(base=a, num=n, start=1, stop=n)
    print(x)

potegi(2, 5)