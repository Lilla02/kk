number = int(input("Kérek egy számot:"))
if number == 5:
    print("kiváló")
elif number == 4:
    print("jó")
elif number == 3:
    print("közepes")
elif number == 2:
    print("elégséges")
elif number == 1:
    print("elégtelen")
else:
    print("nem megfelelő érték")

grade = random.randint(1, 5)
if grade == 5:
    print("kiváló")
elif grade == 4:
    print("jó")
elif grade == 3:
    print("közepes")
elif grade == 2:
    print("elégséges")
elif grade == 1:
    print("elégtelen")
else:
    print("nem megfelelő érték")

print(random.random())