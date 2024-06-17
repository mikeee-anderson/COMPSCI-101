first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

minimum = min(first_number, second_number)
maximum = max(first_number, second_number) + 1
for number in range(minimum, maximum, 1):
    print(number, end=" ")

