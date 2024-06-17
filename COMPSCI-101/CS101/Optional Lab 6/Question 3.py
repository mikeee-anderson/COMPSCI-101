word_1 = input("Enter a first word: ")
word_2 = input("Enter a second word: ")
vowel = "aeiou"
if word_1[-1] == word_2[-1]:
    if (word_1[0] in vowel) and (word_2[0] not in vowel):
            print("Bingo!")
    elif (word_1[0] not in vowel) and (word_2[0] in vowel):
            print("Bingo!")
    else:
        print("Oops!")
else:
    print("Oops!")