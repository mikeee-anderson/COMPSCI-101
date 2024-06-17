print(f"The given list is: {data}")
integer = int(input("Enter an integer from the given list: "))
while integer not in [data]:
    integer = int(input("Enter an integer from the given list: "))

print(f"{integer} is valid.")