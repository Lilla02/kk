menu_command = ""
while menu_command != "0":
    menu_command = input("Kérlek válassz a menüpontok közül:\n\t0 - kilépés\n\t1 - összeadás\n")
    if menu_command == "1":
        a = float(input("Kérlek add meg az első számot: "))
        b = float(input("Kérlek add meg a második számot: "))
        print("A két szám összege:", a +b)
print("Viszlát!")