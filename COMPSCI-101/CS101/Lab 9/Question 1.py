line_of_integers = input("Please enter a line of integers: ")
list_of_integers = line_of_integers.split(',')

total = 0
counter = 0
for integer in list_of_integers:
    integer = int(integer)
    if integer % 2 == 0:
        total += integer
        counter += 1
# round average to two decimal places
if counter > 0:
    average = round(total / counter, 2)
    print(f"The average of the even numbers is {average}.")
else:
    print("The average of the even numbers is undefined.")


