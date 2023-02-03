def perfume_tickets():
    for n in range(1,10000):
        yield f"P - {n}"


def medicine_tickets():
    for n in range(1,10000):
        yield f"M - {n}"


def cosmetic_tickets():
    for n in range(1,10000):
        yield f"C - {n}"


p = perfume_tickets()
m = medicine_tickets()
c = cosmetic_tickets()


def decorator(product):
    print("\n" + "*" * 23)
    print("your number is : ")

    if product == "P":
        print(next(p))
    elif product == "M":
        print(next(m))
    else :
        print(next(c))

    print("please wait for your turn")
    print("*"* 23 + "\n")