words = input("Enter a sequence of words: ")
list_of_words = words.split(" ")
counter = 0
for i in list_of_words:
    if i[0].isupper():
        counter += 1
print(f"{counter} word(s) start with an uppercase letter.")
