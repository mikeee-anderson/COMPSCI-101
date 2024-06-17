word = input("Enter a word: ")

counter = 0
consonants = 0
while counter < len(word):
    word_2 = word[counter]
    if (word_2 != 'a' and word_2 != 'e' and word_2 != 'i' and word_2 != 'o' and word_2 != 'u' and word_2 != 'A' and
            word_2 != 'E' and word_2 != 'I' and word_2 != 'O' and word_2 != 'U'):
        consonants += 1
    counter += 1

print(f"{consonants} consonants.")






