def suma_ciagu(a1=1, r=1, ile=10):
    an=a1+(ile-1)*r
    suma=((a1+an)/2)*ile
    return suma


print(suma_ciagu(10,2,4))