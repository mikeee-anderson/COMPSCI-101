decimal = int(input("Enter the decimal number: "))

if decimal == 0:
    print("0 in decimal is 0 in binary.")
else:
    print(f"{decimal} in decimal is ", end='')
    while decimal > 0:
        if decimal % 2 != 0:
            print("1", end='')
        else:
            print("0", end='')
        decimal = decimal // 2
    print(" in binary.")


