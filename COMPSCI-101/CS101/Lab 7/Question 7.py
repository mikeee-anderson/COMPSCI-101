sentence = input("Please enter a sentence: ")
words = sentence.split(" ")
unique_words = []
counter = 0
while counter < len(words):
    if words[counter] not in unique_words:
        unique_words.append(words[counter])
    counter += 1
unique_words.reverse()
reversed_sentence = ', '.join(unique_words)
print(f"Unique words: {reversed_sentence}")
