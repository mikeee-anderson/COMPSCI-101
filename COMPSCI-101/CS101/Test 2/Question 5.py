import math
number = int(input("Enter a square number: "))
while math.sqrt(number) % 1 != 0:
    number = int(input("Enter a square number: "))

print(f"{number} is the square of {int(math.sqrt(number))}.")


