string = input("Enter the string: ")
char = input("Enter the letter: ")

first_index = 0
while first_index < len(string):
    if string[first_index] == char:
        print(f"The index of the first occurrence of {char} in {string} is {first_index}.")
        break
    else:
        first_index += 1
if first_index == len(string):
    print(f"The letter {char} does not appear in {string}.")
else:
    second_index = -1
    while string[second_index] != char:
        second_index -= 1

    second_index = len(string) + second_index
    print(f"The index of the last occurrence of {char} in {string} is {second_index}.")








