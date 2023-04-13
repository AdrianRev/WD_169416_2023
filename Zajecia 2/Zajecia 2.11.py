n = eval(input("Podaj wysokość diamentu nie większą niż 9 i nie mniejszą niż 3:"))
if n<3 or n>9:
    print("Błędna wysokość")
else:
    if n%2!=0:
        n-=1
    srodek = n//2+1
    for i in range(1, srodek + 1):
        print(" " * (srodek - i) + "O" * (2 * i - 1))
    for i in range(srodek - 1, 0, -1):
        print(" " * (srodek - i) + "O" * (2 * i - 1))