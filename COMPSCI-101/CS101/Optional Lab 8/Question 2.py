text = input("Please enter your text: ")
target_letter = input("Please enter the target_letter: ")

new_word = ""
for i in text:
    if i == target_letter:
        new_word += "*"
    else:
        new_word += i
print(f"Updated text: {new_word}")
