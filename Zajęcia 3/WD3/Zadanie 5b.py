def dodaj_znak(lista):
    lista2=[]
    for i in range(len(lista)):
        lista2.append(lista[i]+"!")
    return lista2


liczby=['jeden','dwa','trzy']
liczby2=dodaj_znak(liczby)
for i in range(len(liczby2)):
    print(liczby2[i])