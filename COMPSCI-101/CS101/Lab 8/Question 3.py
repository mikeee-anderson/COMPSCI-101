text = input("Enter your text: ")
text = text.replace(" ", '')
alphabet_count = 0
digit_count = 0
other_count = 0
for character in text:
    if character.isalpha():
        alphabet_count += 1
    elif character.isdigit():
        digit_count += 1
    else:
        print(character, end="")