Liczby= []

while True:
    a = input("Podaj liczbę lub napisz 'end' by zakończyć:")
    if a == 'end':
        break
    elif a.isdigit():
        Liczby.append(int(a))
    else:
        print("Błędna dana.")
    print("Aktualna lista liczb:",Liczby)

print("Końcowa lista liczb:",Liczby)