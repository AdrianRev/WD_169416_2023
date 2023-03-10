def digital_root(a):
    while a > 9:
        a = sum(int(cyfra) for cyfra in str(a))
    return a


print(digital_root(12432463))
