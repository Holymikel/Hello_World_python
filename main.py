weight = int(input("Weight: "))
pounds_kilo = input("(L)bs or (K)g: ")
if pounds_kilo.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")

