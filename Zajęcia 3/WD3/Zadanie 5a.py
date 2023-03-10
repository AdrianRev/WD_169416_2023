def dodaj_znak(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] + "!"


liczby=['jeden','dwa','trzy']
dodaj_znak(liczby)
for i in range(len(liczby)):
    print(liczby[i])