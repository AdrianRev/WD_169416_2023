def monotonicznosc(a, b):
    if(a > 0):
        print("Funkcja jest rosnąca")
    elif(a == 0):
        print("Funkcja jest stała i y =", b ,"dla dowolnego x")
    else:
        print("Funkcja jest malejąca")


monotonicznosc(0 , 5)