integers = input("Please enter a positive integer or end to stop: ")
numbers = []
while integers != "end":
    integers = int(integers)
    if integers > 0:
        numbers.append(integers)
    integers = input("Please enter a positive integer or end to stop: ")

numbers.sort()
numbers.reverse()
print(f"Positive numbers: {numbers}")






