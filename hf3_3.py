d = str(input("Adja meg a felhasználó nemét(m=fiú/f=lány): "))
proceed = "f"
if d == proceed:
    n = float(input("Adja meg a felhasználó korát: "))
    if n >=10 and n <=12:
        print("A felhasználó felvéve!")
    else:
        print("A felhasználó nem lett felvéve!")
else:
    print("A felhasználó nem lett felvéve!")
