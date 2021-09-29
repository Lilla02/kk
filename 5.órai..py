input_data = input("Kérek egy egész számot.")
try:
    int_number = int(input_data)
    print("A kapott szám 3-szorosa:", 3 * int_number)
    print(type(input_data))
    print(type(int_number))
except valueError:
    print("Ez nem egy egész szám.")