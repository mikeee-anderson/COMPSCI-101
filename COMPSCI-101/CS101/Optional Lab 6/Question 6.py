word = input("Enter a word: ")

index = 0
reverse_index = -1
while index < len(word):
    if word[index] != word[reverse_index]:
        print(f"{word} is not a palindrome.")
        break
    reverse_index -= 1
    index += 1

if index == len(word):
    print(f"{word} is a palindrome.")




