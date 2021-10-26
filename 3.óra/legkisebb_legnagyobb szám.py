a = int(input("Kérek egy számot:"))
b = int(input("Kérek egy számot:"))
c = int(input("Kérek egy számot:"))
print(a, b, c)
if a >= b and a >= c and b >= c:
    print("Az a változó értéke a legnagyobb.")
    print("A c változó értéke a legkisebb.")
elif a >= b and a >= c and c >= b:
    print("Az a változó értéke a legnagyobb.")
    print("A b változó értéke a legkisebb.")
elif b >= a and b >= c and c >= a:
    print("A b változó értéke a legnagyobb.")
    print("Az a változó értéke a legkisebb.")
elif b >= a and b >= c and a >= c:
    print("A b változó értéke a legnagyobb.")
    print("A c változó értéke a legkisebb.")
elif c >= a and c >= b and a >= b:
    print("A c változó értéke a legnagyobb.")
    print("A b változó értéke a legkisebb.")
else:
    print("A c változó értéke a legnagyobb.")
    print("Az a változó értéke a legkisebb.")
