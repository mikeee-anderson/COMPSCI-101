value = input("Enter a value or stop to end: ")

value_list = []
while value != "stop":
    value = float(value)
    value_list += [value]
    value = input("Enter a value or stop to end: ")

threshold = float(input("Enter a threshold value: "))

total = 0
counter = 0
for number in value_list:
    if number > threshold:
        total += number
        counter += 1
average = round(total / counter, 2)
print(f"The average of the values greater than {threshold} is {average}")


