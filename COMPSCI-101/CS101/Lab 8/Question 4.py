lowercase_alpha = "abcdefghijklmnopqrstuvwxyz"
uppercase_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("Please enter your text: ")
print("New Text: ", end='')
for character in text:
    if character in lowercase_alpha:
        character = character.upper()
    elif character in uppercase_alpha:
        character = character.lower()
    print(character, end="")


