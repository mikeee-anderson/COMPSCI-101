sentence = input("Please enter a sequence of words: ")
words = sentence.split(" ")
words.sort(key=str.lower)
counter = 0
for word in words:
    print(f"{counter}. {word.capitalize()}")
    counter += 1
