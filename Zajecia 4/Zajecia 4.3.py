import numpy as np

def tablica(n):
    return np.arange(1, n*n+1).reshape((n, n))

n = input("Podaj rozmiar tablicy:")
tab = tablica(int (n))
print(tab)