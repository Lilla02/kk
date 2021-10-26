number = int(input("Kérek egy számot:"))
if number % 3 == 0 and number % 5 == 0:
    print("Osztható 3-mal is és 5-tel is")
elif number % 3 == 0:
    print("Csak 3-mal osztható")
elif number % 5 == 0:
    print("Csak 5-tel osztható")
else:
    print("Nem osztható sem 3-mal, sem 5-tel")

