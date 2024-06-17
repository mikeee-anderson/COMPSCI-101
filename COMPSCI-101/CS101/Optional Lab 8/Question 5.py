x = int(input("Enter x: "))
n = int(input("Enter n: "))
seperator = " + "
equation = f"1 + {x}"

counter = 2
if (x == 1 or x == 0) and (n == 1 or n == 0):
    total = 0
    print("1 = 1")
else:
    total = 1 + int(x)
    while counter < (n + 1):
        equation = equation + seperator + f"{x}^{counter}"
        total += x ** counter
        counter += 1
    if x != 1 or x!= 0 or n != 1 or n != 0:
        print(f"{equation} = {total}")
