number = int(input("Kérek egy számot:"))
number2 = 100
if number % number2 == 0:
    print("A", number2, "osztója a", number)
else:
    if number2 % number == 0:
        print("A", number, "osztója a", number2)
    else:
        print("Egyik sem osztója a másiknak")
except ValueError:
    print("De én egy számot kértem!")

