sentence = input("Enter a sentence: ")
sentence = sentence.lower()
list_of_words = sentence.split()
new_list = ""
vowels = "aeiou"
new_word = ""
for word in list_of_words:
    if word[0] in vowels:
       new_word = word + "" + "way"
       new_list += (new_word + " ")
    else:
        for i in range(len(word)):
            if word[i] in vowels:
                new_word = word[i:] + word[:i] + "ay"
                break
            elif word[i + 1] == "y":
                new_word = word[i + 1:] + word[:i - 1] + "ay"
                break
        new_list += (new_word + " ")
print(new_list.strip())




