first_name = input("Enter your first name: ")
family_name = input("Enter your family name: ")
number = int(input("Enter a number between 100 and 999: "))

print(f"Your UPI is {first_name[0]}{family_name[0:3]}{number}.")