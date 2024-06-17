number = int(input("Enter any number: "))
result = 1
multiplier = 1
while multiplier <= number:
    result *= multiplier
    if multiplier == number:
        print(f"The factorial of {number} is {result}.")
        break
    else:
        multiplier += 1