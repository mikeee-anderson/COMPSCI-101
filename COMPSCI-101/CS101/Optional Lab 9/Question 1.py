string = input("Enter sentences: ")
new_string = ""

# Flag to indicate if the current character is the first character of a sentence
is_first_char = True

for i in range(len(string)):
    char = string[i]
    if is_first_char and char.isalpha():
        new_string += char.upper()
        is_first_char = False
    else:
        new_string += char

    # If the character is a punctuation mark, set the flag to True for the next character
    if char in ".!?":
        is_first_char = True

print(new_string)