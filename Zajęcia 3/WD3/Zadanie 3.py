import math


def dlugosc_przeciwprostokatnej(a=0, b=0):
    c_kwadrat = a*a+b*b
    c = math.sqrt(c_kwadrat)
    return c


przeciwprostokatna = dlugosc_przeciwprostokatnej(3, 4)
print("Przeciwprostokątna ma długość ", przeciwprostokatna)
