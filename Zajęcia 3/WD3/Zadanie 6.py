import random

def guess_the_number(a=5):
    wynik = 0
    for i in range(0, a):
        a = random.randint(1, 10)
        b = int(input("Zgadnij liczbę od 1 do 10:"))
        print("Wylosowana liczba to:", a)
        if (a == b):
            print("Zdobywasz 10 punktów")
            wynik += 10
        else:
            print("Tracisz punkt")
            wynik -= 1
    print("Koniec gry.Twoja punktacja to", wynik, "pkt.")

guess_the_number()