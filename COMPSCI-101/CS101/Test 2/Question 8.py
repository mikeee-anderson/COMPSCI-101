start = int(input("Enter the range start: "))
end = int(input("Enter the range end: "))

integer = int(input(f"Enter an integer between {start} and {end} (inclusive): "))
total = 0
while integer < start or integer > end:
    total += integer
    integer = int(input(f"Enter an integer between {start} and {end} (inclusive): "))
print(f"The total of all the invalid integers is {total}.")