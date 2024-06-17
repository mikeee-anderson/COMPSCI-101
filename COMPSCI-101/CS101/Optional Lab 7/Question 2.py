text = input("Enter some text: ")

letters = 0
for char in text:
    if char.isalpha():
        letters += 1
print(f"Total letters: {letters}")
