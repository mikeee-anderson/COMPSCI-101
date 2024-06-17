text = input("Please enter your text: ")
alphabet_count = 0
digit_count = 0
other_count = 0
for character in text:
    if character.isalpha():
        alphabet_count += 1
    elif character.isdigit():
        digit_count += 1
    else:
        other_count += 1
print(f"There are {alphabet_count} alphabetic characters.")
print(f"There are {digit_count} digits.")
print(f"There are {other_count} other types of characters")
