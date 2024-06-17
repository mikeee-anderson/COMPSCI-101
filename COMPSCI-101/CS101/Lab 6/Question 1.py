expression = input("Enter an expression: ")

index = 0
counter = 0
pairs = 0

while index < len(expression):
    if expression[index] == '(':
        counter += 1
        index += 1
    elif expression[index] == ')':
        if counter > 0:
            counter -= 1
            pairs += 1
            index += 1
        else:
            print("Incorrect.")
            break
    else:
        index += 1
else:
    if counter == 0:
        print("Correct.")
        print(f"There are {pairs} pairs of parentheses.")
    else:
        print("Incorrect.")