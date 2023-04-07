import numpy as np

m1 = np.random.randint(low=10, high=50, size=(3, 3))
m2 = np.random.randint(low=10, high=50, size=(4, 4))

print(m1)
print("Najniższe wartości dla każdego wiersza:")
print(m1.min(axis=1))
print("Najniższe wartości dla każdej kolumny:")
print(m1.min(axis=0))

print("_______________")

print(m2)
print("Najniższe wartości dla każdego wiersza:")
print(m2.min(axis=1))
print("Najniższe wartości dla każdej kolumny:")
print(m2.min(axis=0))