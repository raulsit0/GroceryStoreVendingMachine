import numbersgen


def ask():
    print("welcome to python drug store")

    while True:
        print("[P] - Perfume \n[M] -Medicine \n[C] - Cosmetics \n")
        try:
            my_product = input("choose your Product: ").upper()
            ["P", "M", "C"].index(my_product)
        except ValueError:
            print("That is not a valid option")
        else:
            break

    numbersgen.decorator(my_product)

def start():
    while True:
        ask()
        try:
            another_ticket =input("do you want another ticket? [Y],[N}").upper()
            ["Y", "N"].index(another_ticket)
        except ValueError:
            print("not a valid option")
        else:
            if another_ticket == "N":
                print("Thank you for visiting our python  drug store")
                break

start()