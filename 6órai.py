is_number = False
while not is_number:
    try:
        number = int(input("Kérlek adj meg egy számot: "))
        if number % 2 == 0:
            print("A szám páros.")
        else:
            print("A szám páratlan.")
    except ValueError:
        print("Input is not integer")
    