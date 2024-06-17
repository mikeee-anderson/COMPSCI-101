word = input("Enter a word: ")

if len(word) > 1:
    word = word[0].upper() + word[1:-1].lower() + word[-1].upper()
else:
    word = word.upper()

print(f"The converted word is: {word}.")
