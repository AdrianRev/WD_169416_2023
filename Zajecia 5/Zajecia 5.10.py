import numpy as np

mat=np.arange(81).reshape(9,9)
print(mat)
mat=mat.reshape(3,27)
print(mat)
#Możliwymi przekształceniami macierzy 9x9 są jedynie takie macierze axb że a*b=81