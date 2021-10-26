a = int(input("Kérek egy számot:"))
b = int(input("Kérek egy számot:"))
c = int(input("Kérek egy számot:"))
print(a, b, c)
if a + b > c and a + c > b and b + c > a:
    print("Lehet ezen oldalhosszakkal háromszöget szerkeszteni.")
else:
    print("Nem lehet ezen oldalhosszakkal háromszöget szerkeszteni.")

a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
print(a, b, c)
if a + b > c and a + c > b and b + c > a:
    print("Lehet ezen oldalhosszakkal háromszöget szerkeszteni.")
else:
    print("Nem lehet ezen oldalhosszakkal háromszöget szerkeszteni.")
