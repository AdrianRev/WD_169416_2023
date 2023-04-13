a = float(input("Podaj wartość liczby a: "))
b = float(input("Podaj wartość liczby b: "))
c = float(input("Podaj wartość liczby c: "))
if a>0 and a<=10 and (a>b or b>c):
    print("Podane liczby spełniają warunki")
else:
    print("Podane liczby nie spełniają warunków")