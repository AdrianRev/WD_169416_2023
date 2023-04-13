liczby = input("Podaj liczby oddzielone spacjami: ").split()

liczby = [int(x) for x in liczby]

for i in liczby:
    print(i**2)