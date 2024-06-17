line_of_integers = input("Enter a line of integer values: ")
integers_list = line_of_integers.split(",")

positive_integers = []
for integer in integers_list:
    integer = int(integer)
    if integer % 2 == 0:
        positive_integers += [str(integer)]

print("The even integers are:", ", ".join(positive_integers))





