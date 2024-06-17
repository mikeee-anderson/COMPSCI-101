sentence = input("Enter a sentence: ")

forward = ""
reverse = ""
for char in sentence:
    if char.isalpha():
        char = char.lower()
        forward += char

for char in reversed(sentence):
    if char.isalpha():
        char = char.lower()
        reverse += char

counter = 0
while counter < len(forward):
    if forward[counter] != reverse[counter]:
        print(f'"{sentence}" is not a palindrome')
        break
    counter += 1

if counter == len(forward):
    print(f'"{sentence}" is a palindrome')