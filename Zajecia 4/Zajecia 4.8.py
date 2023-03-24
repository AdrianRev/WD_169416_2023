import numpy as np

def f(mat, kierunek='poziomo'):
    if kierunek == 'poziomo':
        if mat.shape[0] % 2 != 0:
            print("Ilosc wierszy nie pozwala na operacje")
        else:
            polowa = int(mat.shape[0] / 2)
            return  mat[:polowa,:],mat[polowa:,:]
    elif kierunek=='pionowo':
        if mat.shape[1] % 2 != 0:
            print("Ilosc kolumn nie pozwala na operacje")
        else:
            polowa = int(mat.shape[1] / 2)
            return mat[:,:polowa],mat[:,polowa:]

mat=np.arange(36)
mat=mat.reshape((6,6))
print(mat)

mat1,mat2 =f(mat, kierunek='pionowo')
print(mat1)

print(mat2)