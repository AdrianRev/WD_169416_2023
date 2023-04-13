n = eval(input("Podaj wysokość wieży nie większą niż 10:"))
if n<=10 and n>0:
    for i in range(1, n + 1):
        print("A" * i)
else:
    print("Błędna wysokość wieży")
