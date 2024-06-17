number1 = float(input("Enter first number: "))
operator = input("Enter one of the following (+, -, *, /): ")
number2 = float(input("Enter second number: "))

if operator == '+':
    result = number1 + number2
    print(result)
elif operator == '-':
    result = number1 - number2
    print(result)
elif operator == '*':
    result = number1 * number2
    print(result)
elif operator == '/':
    result = number1 / number2
    print(result)

continue_calculation = input("Do you have ane extra calculation, if not enter 'q'.")
while continue_calculation != 'q':
    number1 = float(input("Enter first number: "))
    operator = input("Enter one of the following (+, -, *, /): ")
    number2 = float(input("Enter second number: "))
    if operator == '+':
        result = number1 + number2
        print(result)
    elif operator == '-':
        result = number1 - number2
        print(result)
    elif operator == '*':
        result = number1 * number2
        print(result)
    elif operator == '/':
        result = number1 / number2
        print(result)
    continue_calculation = input("Do you have ane extra calculation, if not enter 'q'.")
    if continue_calculation != 'q':
        continue
    else:
        break
