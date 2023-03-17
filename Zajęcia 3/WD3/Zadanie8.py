import random

def multipli_game(ile=10):
    poprawne=0
    niepoprawne=0
    for i in range(0,ile):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = input(f"{a} x {b} = ")
        if(int(c) == a * b):
            print("Poprawna odpowiedź")
            poprawne += 1
        else:
            print("Błędna odpowiedź")
            niepoprawne += 1
    print(f"Twój wynik to {poprawne} poprawnych i {niepoprawne} błędnych odpowiedzi.")


multipli_game()