user_integer = int(input("Enter an integer: "))
total = 0
for number in range(0, user_integer, 2):
    total += number
print(f"The result of the sum  is {total}.")