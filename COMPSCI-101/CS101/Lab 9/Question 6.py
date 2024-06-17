line_of_integer = input("Enter a line of integers: ")
line_of_integer = line_of_integer.strip()
integer_list = line_of_integer.split(',')

# Check if this application of for  in loop is correct
# Check how to use for...in + range() function
updated_list = []
for integer in integer_list:
    integer = int(integer)
    updated_list += [integer]

minimum = min(updated_list)
maximum = max(updated_list)
print(f"The minimum number is {minimum} and the maximum number is {maximum}.")
